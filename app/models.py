from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    telegram_id = models.BigIntegerField(unique=True, null=True, blank=True)
    role = models.CharField(max_length=10,
                            choices=ROLE_CHOICES,
                            default='student')

