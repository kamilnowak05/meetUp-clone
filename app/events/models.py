from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from groups.models import AppGroup

User = get_user_model()


class EventCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/images', blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    owner_group = models.ForeignKey(
        AppGroup,
        related_name='owner_group',
        on_delete=models.CASCADE
        )
    title = models.CharField(max_length=240)
    about = models.TextField()
    image = models.ImageField(
        upload_to='events/images',
        blank=True,
        null=True
        )
    category = models.ForeignKey(
        EventCategory,
        related_name='event_category',
        on_delete=models.CASCADE
        )
    member = models.ManyToManyField(
        User,
        related_name="members"
        )
    location = models.CharField(max_length=240)
    event_date = models.DateField()
    event_time_start = models.CharField(max_length=5)
    event_time_end = models.CharField(max_length=5)
    chief_guest = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
        )

    def __str__(self):
        return self.title


class EventReview(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_review',
        on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        Event,
        related_name='event_review',
        on_delete=models.CASCADE
        )
    rating = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
        )
    review = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event.title


# class EventMember(models.Model):
#     user = models.ManyToManyField(
#         'users.User',
#         related_name="member"
#         )
#     event = models.ForeignKey(
#         Event,
#         related_name='event',
#         on_delete=models.CASCADE
#         )
#     quantity = models.PositiveIntegerField(default=1)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.event.title


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
