from rest_framework import serializers
from .models import Partner
from .services.utils import check_cnpj
from django.core.validators import FileExtensionValidator
import csv


class PartnerSerializer(serializers.ModelSerializer):
    cnpj = serializers.CharField(validators=[])

    class Meta:
        model = Partner
        fields = "__all__"

    def validate_cnpj(serlf, value):
        value = "".join(filter(str.isdigit, value))
        if not check_cnpj(value):
            raise serializers.ValidationError("Invalid cnpj")
        return value

    def create(self, validated_data):
        cnpj = validated_data.get("cnpj")
        partner, created = Partner.objects.update_or_create(
            cnpj=cnpj, defaults=validated_data
        )
        return partner, created


class ImportPartnerSerializer(serializers.Serializer):
    data = serializers.FileField(allow_empty_file=False, validators=[
                                FileExtensionValidator(allowed_extensions=['csv']),
                            ])

    def create(self, validated_data):
        csv_file = validated_data["data"]
        decoded_file = csv_file.read().decode("utf-8").splitlines()
        decoded_file[0] = self.columns_name_to_snake_case(decoded_file[0])
        reader = csv.DictReader(decoded_file)

        for row in reader:
            data = self.row_to_model_alias(row)
            serializer = PartnerSerializer(data=data)
            if serializer.is_valid():
                instance, create = serializer.save()
        return True

    def columns_name_to_snake_case(self, columns):
        column = columns.strip()
        words = column.split(",")
        snake_case = ",".join(word.strip().lower().replace(" ", "_") for word in words)

        return snake_case

    def row_to_model_alias(self, row):
        cnpj = "".join(filter(str.isdigit, row.get("cnpj", None)))
        return {
            "cnpj": cnpj,
            "name": row.get("razão_social", None),
            "trade_name": row.get("nome_fantasia", None),
            "phone": row.get("telefone", None),
            "email": row.get("email", None),
            "zip_code": row.get("cep", None),
        }
