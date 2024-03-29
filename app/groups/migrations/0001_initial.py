# Generated by Django 2.2.3 on 2019-08-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AppGroup",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("group_image", models.ImageField(blank=True, upload_to="groups/images")),
                (
                    "group_category",
                    models.ManyToManyField(blank=True, related_name="group_category", to="events.EventCategory"),
                ),
            ],
        ),
    ]
