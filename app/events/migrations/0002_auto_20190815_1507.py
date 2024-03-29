# Generated by Django 2.2.3 on 2019-08-15 15:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("groups", "0001_initial"),
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventreview",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="user_review", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="event_category", to="events.EventCategory"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="member",
            field=models.ManyToManyField(related_name="members", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="event",
            name="owner_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="owner_group", to="groups.AppGroup"
            ),
        ),
    ]
