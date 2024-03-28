from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class CustomUser(AbstractUser):
    
    uuid  = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    full_name = models.CharField(max_length=9999)
    phone = models.CharField(max_length=20,blank=True)
    isEmailVerified = models.BooleanField(default=False)

    def __str__(self):
        return self.username