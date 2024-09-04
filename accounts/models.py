from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid
from .managers import CustomUserManager
# Create your models here.
class User(AbstractUser):
    
    USER_TYPE = [
        ('renter' , 'Renter'),
        ('owner', 'Owner'),
        ('agent', 'Agent'),
        ('builder', 'Builder'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.CharField(max_length=7, choices=USER_TYPE, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    more_data = models.JSONField(default=dict, blank=True, null=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']

    def __str__(self):
        return self.email
    
class TimeStampedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    more_data = models.JSONField(default=dict, blank=True, null=True)

    class Meta:
        abstract = True