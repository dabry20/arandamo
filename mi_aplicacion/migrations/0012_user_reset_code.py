# Generated by Django 5.0.7 on 2024-10-25 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0011_reportes_created_reportes_updated_recomendacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reset_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]