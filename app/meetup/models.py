import uuid

from django.db import models
from django.utils import timezone



MY_INTERESTS = (
                ('Ad','Adventure'),
                ('Fd','Food'),
                ('Th','Tech'),
                ('Fy','Family'),
                ('Ht','Health'),
                ('St','Sports'),
                ('Fi','Film'),
                ('Bk','Books'),
                ('De','Dance'),
                ('Ar','Arts'),
                )


class Interest(models.Model):
    interest = models.CharField(max_length=255,blank=False, null=False)

    def __str__(self):
        return self.interest


class Group(models.Model):
    name = models.CharField(max_length=255,blank=False, null=False)
    group_id = models.UUIDField(unique=True, default=uuid.uuid4)
    creator = models.ForeignKey('core.User', on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(Interest, on_delete=models.CASCADE)
    location = models.CharField(max_length=55,blank=False, null=False)

    def __str__(self):
        return self.name


class GroupMemberDetails(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        str = "{} {}".format(self.user.email,self.group.name)
        return str


class Meetup(models.Model):
    name = models.CharField(max_length=255,blank=False, null=False)
    meetup_id = models.UUIDField(unique=True, default=uuid.uuid4)
    host = models.ForeignKey('core.User', on_delete=models.CASCADE)
    group = models.ForeignKey(Group ,on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    fee = models.IntegerField(default=0)
    slots = models.IntegerField(default= 10)

    def __str__(self):
        return self.name

class MeetupMemberDetails(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    meetup = models.ForeignKey(Meetup, on_delete=models.CASCADE)

    def __str__(self):
        str = "{} {}".format(self.user.email,self.meetup.name)
        return str

class WaitingList(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    meetup = models.ForeignKey(Meetup, on_delete=models.CASCADE)

    def __str__(self):
        str = "{} {}".format(self.user.email,self.meetup.name)
        return str
