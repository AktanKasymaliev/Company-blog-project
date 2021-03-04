from rest_framework import generics
from .models import *
from .serializers import *
from .pagination import ListPagination
from django_filters.rest_framework import DjangoFilterBackend


class CompanyView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = ListPagination
    
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('company_name', 'address', 'owner__username')
    search_fields = ('company_name', 'address', 'owner__username')

class CompanyCreate(generics.CreateAPIView):
    serializer_class = CompanyCreateSerializer

    def get_serializer_context(self):
        context = super(CompanyCreate, self).get_serializer_context()
        context.update({
            'owner':self.request.user
        })
        return context

class CompanyDetail(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer

#Advertisment vews

class AdvertismentView(generics.ListAPIView):
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentViewSerializer
    pagination_class = ListPagination
    
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('company', 'title',)
    search_fields = ('company', 'title',)

class AdvertismentCreate(generics.CreateAPIView):
    serializer_class = AdvertismentCreateSerializer
    
    def get_serializer_context(self):
        context = super(AdvertismentCreate, self).get_serializer_context()
        return context

class AdvertismentDetail(generics.RetrieveAPIView):
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentDetailSerializer    
