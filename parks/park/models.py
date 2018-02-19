from django.db import models
from django.utils import timezone

class Photo(models.Model):
    photourl = models.CharField(max_length=500)

    def __str__(self):
        return self.photourl

class Review(models.Model):
    review_text = models.TextField(null=True, blank=True)
    mark = models.NullBooleanField()

    def __str__(self):
        return self.review_text

class Park(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)
    photos = models.ManyToManyField(Photo, blank=True)
    rating = models.FloatField(null=True)
    formatted_address = models.CharField(max_length=200, null=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
       return self.title