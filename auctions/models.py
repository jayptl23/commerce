from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="listings")
