from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True)
    age = models.PositiveIntegerField(default=18)
    image = models.ImageField(upload_to='user/profile')


    def __str__(self):
        return self.full_name
