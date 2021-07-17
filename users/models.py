from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=64, blank=False, unique=True)
    phone = PhoneNumberField(blank=False)
    photo = models.ImageField(blank=True)
