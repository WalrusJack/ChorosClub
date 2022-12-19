from django.db import models
from django.contrib.auth.models import User

EVENT_TYPES = (
    ('Art', 'Art'),
    ('Bar', 'Bar'),
    ('Camping', 'Camping'),
    ('Entertainment', 'Entertainment'),
    ('Festival', 'Festival'),
    ('Food', 'Food'),
    ('Hiking', 'Hiking'),
    ('Music', 'Music'),
    ('Nature', 'Nature'),
    ('Scenery', 'Scenery'),
    ('Sports', 'Sports'),
    ('Theatre', 'Theatre'),
    ('Other', 'Other'),
)


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=1000, blank=True)

    def __string__(self):
        return self.user.username


class Place(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)
    type = models.CharField(max_length=128, choices=EVENT_TYPES)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place')
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, related_name='logs', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
