from django.contrib import admin

# Register your models here.
from .models import Camera


class Camerapost(admin.ModelAdmin):
    list_display = ('id', 'name', 'Barcode', 'Enddateofwarranty')
    search_fields = ('name', 'Barcode')

admin.site.register(Camera, Camerapost)
