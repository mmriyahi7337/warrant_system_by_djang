# Generated by Django 2.2.6 on 2019-11-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlypage', '0003_auto_20191103_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='Barcode',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='شماره سریال'),
        ),
    ]
