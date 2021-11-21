from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    age = models.PositiveIntegerField(default=18)
    image = models.ImageField(upload_to='user/profile')

    def str(self):
        return self.first_name
