# Generated by Django 5.0.7 on 2024-10-25 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0012_user_reset_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='reset_code',
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='token_expires',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
