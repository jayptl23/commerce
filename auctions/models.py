from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=10, validators=[MinValueValidator(1)])
    image_url = models.URLField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="listings")
    
    def __str__(self):
        return f"{self.pk}: {self.title}"

class User(AbstractUser):
    watchlist = models.ManyToManyField(Listing, blank=True, related_name="watched_by")
