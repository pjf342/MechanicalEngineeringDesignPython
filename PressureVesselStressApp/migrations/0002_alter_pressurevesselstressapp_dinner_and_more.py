# Generated by Django 4.0.5 on 2022-06-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PressureVesselStressApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressurevesselstressapp',
            name='dinner',
            field=models.FloatField(max_length=100, verbose_name='Inner Diameter'),
        ),
        migrations.AlterField(
            model_name='pressurevesselstressapp',
            name='douter',
            field=models.FloatField(max_length=100, verbose_name='Outer Diameter'),
        ),
        migrations.AlterField(
            model_name='pressurevesselstressapp',
            name='pinner',
            field=models.FloatField(max_length=100, verbose_name='Inner Pressure'),
        ),
        migrations.AlterField(
            model_name='pressurevesselstressapp',
            name='pouter',
            field=models.FloatField(max_length=100, verbose_name='Outer Pressure'),
        ),
    ]