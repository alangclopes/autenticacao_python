# Generated by Django 5.1 on 2024-09-01 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0001_initial'),
        ('otp_totp', '0003_add_timestamps'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp_device',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_otp_device', to='otp_totp.totpdevice'),
        ),
    ]
