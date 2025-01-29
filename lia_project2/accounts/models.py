from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
import re

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True)
    bio = models.TextField(blank=True, max_length=100)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.validate_email(self.email)
            self.validate_password(self.password)
            self.set_password(self.password)
        super().save(*args, **kwargs)

    @staticmethod
    def validate_email(email):
        """Validate email using regex to ensure proper formatting."""
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, email):
            raise ValidationError("Invalid email: Please enter a valid email address.")

    @staticmethod
    def validate_password(password):
        if not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password):
            raise ValidationError("Password must contain both letters and numbers.")
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

    def __str__(self):
        return self.username