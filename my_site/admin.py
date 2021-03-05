from django.contrib import admin
from .models import *


class AdImageInline(admin.TabularInline):
    model = AdvertismentImages 
    fields = ('image', 'description')



@admin.register(Advertisment)
class AdvertismentAdmin(admin.ModelAdmin):
    inlines = [AdImageInline,]

admin.site.register(Company)