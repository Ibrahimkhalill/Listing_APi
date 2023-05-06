from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    title = models.CharField(max_length=100)
    pictures = models.ImageField(upload_to='image')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    guests = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    amenities = models.TextField(blank=True)
    available_dates = models.DateField(blank=True,null=True)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')

    def __str__(self):
      return self.title