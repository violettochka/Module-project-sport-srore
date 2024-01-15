from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    wallet = models.IntegerField(null=True, blank=True, default=10000)

    


