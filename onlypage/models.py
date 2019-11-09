from django.db import models
from django_jalali.db import models as jmodels


# Create your models here.
class Camera(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)

    Startdayofwarranty = jmodels.jDateField(verbose_name='تاریخ شروع گارانتی')
    Enddateofwarranty = jmodels.jDateField(verbose_name='تاریخ اتمام گارانتی')
    Barcode = models.CharField(max_length=20, blank=True, verbose_name='شماره سریال')

    def __str__(self):
        return self.name

    @property
    def barcode(self):
        return self.Barcode
