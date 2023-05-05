from rest_framework import viewsets, parsers
from .models import Partner
from .serializers import ImportPartnerSerializer, PartnerSerializer
from django.shortcuts import render
from django.http import JsonResponse

class ImportPartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = ImportPartnerSerializer
    parser_classes = (parsers.MultiPartParser,)

    def create(self, request, *args, **kwargs):

        file = request.data
        serializer = self.serializer_class(data=file)
        serializer.is_valid()
        serializer.save()
        
        part = Partner.objects.all()
        return JsonResponse({'status': 'success'})



class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()



def upload_file(request):
    return render(None, 'import_partners.html')