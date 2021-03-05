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

class CompanyEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_name', 'logo', 'address', 'phone', 'info')



# Advertisment serializers
class AdvertismentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisment
        fields = ('company', 'title', 'body', 'created_at','id')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = instance.images.count()
        representation['company'] = instance.company.company_name
        return representation

class AdvertismentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisment
        fields = ('title', 'body', 'company')
    

class AdvertismentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisment
        fields = ('company', 'title', 'body', 'created_at','id')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = instance.images.count()
        representation['company'] = instance.company.company_name
        return representation

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertismentImages
        fields = ('image', 'description')


class AdvertismentEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisment
        fields = ('title', 'body', 'company')




