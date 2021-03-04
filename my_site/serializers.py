from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('owner', 'company_name', 'logo', 'address', 'phone', 'info', 'id')

class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_name', 'logo', 'address', 'phone', 'info')

    def create(self, validated_data):
        owner = self.context.get('owner')
        company = Company.objects.create(owner=owner, **validated_data)
        company.save()
        return company

class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('owner', 'company_name', 'logo', 'address', 'phone', 'info', 'id')



# Advertisment serializers
class AdvertismentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisment
        fields = ('company', 'title', 'body', 'image', 'id')

class AdvertismentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisment
        fields = ('company','title', 'body', 'image')
    
    def create(self, validated_data):
        advert = Advertisment.objects.create(**validated_data)
        advert.save()
        return advert

class AdvertismentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisment
        fields = ('company', 'title', 'body', 'image', 'id')



