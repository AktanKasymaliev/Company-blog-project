from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCompanyOwner

from .models import *
from .serializers import *
from django.db.models import Q 
from .pagination import ListPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response




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



class CompanyEdit(generics.UpdateAPIView):
    serializer_class = CompanyEditSerializer
    queryset = Company.objects.all()


#Advertisment vews
class AdvertismentView(generics.ListAPIView):
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentViewSerializer
    pagination_class = ListPagination
    lookup_field = 'pk'
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('company__company_name', 'title',)
    # search_fields = ('company__company_name', 'title',)
    def get_queryset(self):
        filter_ = self.request.query_params.get('filter')
        queryset = super().get_queryset() # - получаем queryset Advertisment
        queryset = queryset.filter(Q(title__icontains=filter_) | Q(body__icontains=filter_)) # - фильтруем
        return queryset

class AdvertismentCreate(generics.CreateAPIView):
    serializer_class = AdvertismentCreateSerializer
    permission_classes = [IsAuthenticated,]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        company = Company.objects.get(pk=request.data['company'])
        if company.owner == self.request.user:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"OK"}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"You do not have permissions"}, status=status.HTTP_400_BAD_REQUEST)

class AdvertismentDetail(generics.RetrieveAPIView):
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentDetailSerializer    


class AdvertismentEdit(generics.UpdateAPIView):
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentEditSerializer
    http_method_names = ['patch', ]
    permission_classes = [IsCompanyOwner]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = AdvertismentImages.objects.all()
    serializer_class = ImageSerializer

    @action(detail=False, methods=['GET',])
    def search(self, request, pk=None):
        q = request.query_params.get('q')  # request.query_params = request.GET 
        queryset = super().get_queryset() # - получаем queryset AdImage 
        queryset = queryset.filter(description__icontains=q) # - фильтруем
        serializer = ImageSerializer(queryset, many=True) #  - сериализирует в API полученный quryset
        return Response(serializer.data, status=status.HTTP_200_OK) # - возвращает их