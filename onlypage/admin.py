from django.contrib import admin

# Register your models here.
from .models import Camera
from import_export import resources, fields
from import_export.widgets import Widget
from import_export.admin import ImportExportActionModelAdmin
from khayyam import JalaliDate,JalaliDatetime


class CustomDateWidget(Widget):

    def __init__(self, format=None):
        super().__init__()

    def clean(self, value, row=None, *args, **kwargs):

        for i in value:
            date = value.split("-")
            value = JalaliDatetime(date[0], date[1], date[2])

            now = JalaliDate(value).todate()
            value = str(now)

            return value




class Camerapost(resources.ModelResource):
    st = fields.Field(
        column_name='Startdayofwarranty',
        attribute='Startdayofwarranty',
        widget=CustomDateWidget()
    )
    et = fields.Field(
        column_name='Enddateofwarranty',
        attribute='Enddateofwarranty',
        widget=CustomDateWidget()
    )

    class Meta:
        model = Camera
        fields = ('id', 'name', 'st', 'et', 'Barcode')
        export_order = ('id','name','st','et','Barcode')
        import_id_fields = ('id',)
        # exclude = ('id',)


class CustomBookAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name', 'Barcode', 'Enddateofwarranty')
    search_fields = ('name', 'Barcode')
    resource_class = Camerapost
    pass


admin.site.register(Camera, CustomBookAdmin)

