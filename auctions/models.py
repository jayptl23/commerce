from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings


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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=2, on_delete=models.CASCADE, related_name="listings")
    is_open = models.BooleanField(default=True)
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None, on_delete=models.CASCADE, related_name="won_listings")

    def __str__(self):
        return f"{self.pk}: {self.title}"

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.created_at}"

class User(AbstractUser):
    watchlist = models.ManyToManyField(Listing, blank=True, related_name="watched_by")

    def __str__(self):
        return f"User ID: {self.id}"

class Bid(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=10, validators=[MinValueValidator(1)])
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"bid_id={self.pk} amount={self.amount}"
