from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AppGroup(models.Model):
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    group_category = models.ManyToManyField("events.EventCategory", related_name="group_category", blank=True)
    description = models.TextField()
    group_image = models.ImageField(upload_to="groups/images", blank=True)
    member = models.ManyToManyField(User, related_name="group_members")

    def __str__(self):
        return self.name
