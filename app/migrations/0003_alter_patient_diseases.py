# Generated by Django 4.2.4 on 2023-09-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_special_patient_diseases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Diseases',
            field=models.CharField(max_length=10),
        ),
    ]
