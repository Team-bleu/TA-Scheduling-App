# Generated by Django 2.1.2 on 2018-11-26 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TA_Scheduling_App', '0004_auto_20181125_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='labs',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='class',
            name='ta',
            field=models.CharField(default='None', max_length=50),
        ),
    ]