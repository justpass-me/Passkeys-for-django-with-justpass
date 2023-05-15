from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    token = models.CharField(max_length=64,default=None,null=True)
    mfa_enabled = models.BooleanField(default=None,null=True)
    REQUIRED_FIELDS=['first_name','last_name','phone_number']