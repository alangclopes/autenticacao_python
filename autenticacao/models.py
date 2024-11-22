from django.db import models
from django.contrib.auth.models import AbstractUser
from django_otp.plugins.otp_totp.models import TOTPDevice

class User(AbstractUser):
    otp_device = models.OneToOneField(TOTPDevice, on_delete=models.CASCADE, null=True, blank=True, related_name='user_otp_device')