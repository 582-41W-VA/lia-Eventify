from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True)
    bio = models.TextField(blank=True, max_length=100)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username