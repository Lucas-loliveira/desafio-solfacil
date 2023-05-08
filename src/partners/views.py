from typing import Any, Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import parsers, status, viewsets
from rest_framework.response import Response

from .models import Partner
from .serializers import ImportPartnerSerializer, PartnerSerializer


class ImportPartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = ImportPartnerSerializer
    parser_classes = (parsers.MultiPartParser,)

    def create(self, request: HttpRequest, *args: Any, **kwargs: Any) -> Response:
        file = request.data
        serializer = self.serializer_class(data=file)
        if serializer.is_valid():
            result = serializer.save()
            return Response(data=result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


def upload_file(request):
    return render(None, "import_partners.html")
