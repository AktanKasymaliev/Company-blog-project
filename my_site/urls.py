from django.urls import path
from .views import *


urlpatterns = [
    path('list/', CompanyView.as_view(), name='company_view'),
    path('create/', CompanyCreate.as_view(), name='company_name'),
    path('<int:pk>/', CompanyDetail.as_view(), name='company_detail'),
    #Advertisment paths 
    path('list/ad/', AdvertismentView.as_view(), name='advertisment'),
    path('create/ad/', AdvertismentCreate.as_view(), name='create_advertisment'),
    path('detail/ad/<int:pk>/', AdvertismentDetail.as_view(), name='detail_advertisment'),
]