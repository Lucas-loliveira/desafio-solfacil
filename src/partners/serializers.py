import csv
from typing import Dict, List, Tuple

from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from .models import Partner
from .services.utils import check_cnpj
from .services.zipcode_client import ZipCodeApi

class PartnerSerializer(serializers.ModelSerializer):
    cnpj: serializers.CharField = serializers.CharField(validators=[])

    class Meta:
        model = Partner
        fields: str = "__all__"

    def validate_cnpj(self, value: str) -> str:
        value = "".join(filter(str.isdigit, value))
        if not check_cnpj(value):
            raise serializers.ValidationError("Invalid cnpj")
        return value

    def validade_zip_code(self, value: str) -> str:
        value = "".join(filter(str.isdigit, value))
        return value

    def create(self, validated_data: Dict) -> Tuple[Partner, bool]:
        if ( "zip_code" in validated_data):
            zip_code_api = ZipCodeApi()
            if address := zip_code_api.get_address(validated_data.get("zip_code")):
                validated_data["city"] = address.get("localidade", None)
                validated_data["state"] = address.get("uf", None)

        cnpj = validated_data.get("cnpj")
        partner, created = Partner.objects.update_or_create(
            cnpj=cnpj, defaults=validated_data
        )
        return partner, created


class ImportPartnerSerializer(serializers.Serializer):
    data: serializers.FileField = serializers.FileField(
        allow_empty_file=False,
        validators=[
            FileExtensionValidator(allowed_extensions=["csv"]),
        ],
    )

    def create(self, validated_data: Dict) -> Dict[str, List[Dict]]:
        csv_file = validated_data["data"]
        decoded_file = csv_file.read().decode("utf-8").splitlines()
        decoded_file[0] = self.columns_name_to_snake_case(decoded_file[0])
        reader = csv.DictReader(decoded_file)

        created_list = []
        updated_list = []
        error_list = []
        for row in reader:
            data = self.row_to_model_alias(row)
            serializer = PartnerSerializer(data=data)
            if serializer.is_valid():
                instance, created = serializer.save()
                if created:
                    created_list.append({"id": instance.id, "cnpj": instance.cnpj})
                else:
                    updated_list.append({"id": instance.id, "cnpj": instance.cnpj})
            else:
                error_list.append({**data, "errors": serializer.errors})

        return {"created": created_list, "updated": updated_list, "errors": error_list}

    def columns_name_to_snake_case(self, columns: str) -> str:
        column = columns.strip()
        words = column.split(",")
        snake_case = ",".join(word.strip().lower().replace(" ", "_") for word in words)

        return snake_case

    def row_to_model_alias(self, row: Dict) -> Dict[str, str]:
        cnpj = "".join(filter(str.isdigit, row.get("cnpj", None)))
        return {
            "cnpj": cnpj,
            "name": row.get("razão_social", None),
            "trade_name": row.get("nome_fantasia", None),
            "phone": row.get("telefone", None),
            "email": row.get("email", None),
            "zip_code": row.get("cep", None),
        }
