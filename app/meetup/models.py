import uuid

from django.db import models
from core.models import User, CATEGORY


class EventCategory(models.Model):
    category = models.CharField(max_length=2, choices=CATEGORY)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category/images')

    def __str__(self):
        return self.category


class Event(models.Model):
    user = models.ForeignKey(User, related_name='event_user', on_delete=models.CASCADE)
    title = models.CharField(max_length=240)
    about = models.TextField()
    image = models.ImageField(upload_to='events/images', blank=True, null=True)
    category = models.ForeignKey('EventCategory', related_name='event_category',
                                        on_delete=models.CASCADE)
    location = models.CharField(max_length=240)
    event_date = models.DateField()
    ticket_amount_first = models.DecimalField(max_digits=1000, decimal_places=2)
    ticket_amount_second = models.DecimalField(max_digits=1000, decimal_places=2)
    event_time_start = models.CharField(max_length=5)
    event_time_end = models.CharField(max_length=5)
    chief_guest = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    #company info bellow
    company_name = models.CharField(max_length=240)
    company_phone1 = models.CharField(max_length=20)
    company_phone2 = models.CharField(max_length=20, blank=True, null=True)
    company_email = models.EmailField()
    company_address = models.CharField(max_length=240)
    company_office = models.CharField(max_length=240)
    company_web_address = models.URLField(max_length=200, blank=True, null=True)
    rating = models.PositiveIntegerField(default=0)

    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class EventReview(models.Model):
    user = models.ForeignKey(User, related_name='user_review', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', related_name='event_review', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)
    review = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event.title

class EventBooking(models.Model):
    user = models.ForeignKey(User, related_name="user_booking", on_delete=models.CASCADE)
    event = models.ForeignKey('Event', related_name='event_booking', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email


from django.db.models.signals import post_save
import math

def average_rating(sender, instance, *args, **kwargs):
    qs = EventReview.objects.filter(event=instance.event.id)
    reviews = [review.rating for review in qs]
    a = 0
    for i in reviews:
        a += i
    average = (a/len(reviews))
    event_obj = qs[0].event
    event_obj.rating = average
    event_obj.save()

post_save.connect(average_rating, sender=EventReview)