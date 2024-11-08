# Generated by Django 5.0.7 on 2024-10-25 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0010_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportes',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reportes',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name='Recomendacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rclimaticas', models.TextField()),
                ('rsuelo', models.TextField()),
                ('ragronomicas', models.TextField()),
                ('rfenologicos', models.TextField()),
                ('rplagas', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('reporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recomendaciones', to='mi_aplicacion.reportes')),
            ],
        ),
    ]
