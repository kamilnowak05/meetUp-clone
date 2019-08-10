# from django.db import models
# from users.models import User

#
# class AppGroup(models.Model):
#     owner = models.ForeignKey(User, related_name='owner')
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     members = models.ManyToManyField(User, related_name='members')
    # group_image = models.ImageField(upload_to='groups/images', blank=True)
    # phone1 = models.CharField(max_length=20)
    # phone2 = models.CharField(
    #     max_length=20,
    #     blank=True,
    #     null=True
    # )
    # email = models.EmailField()
    # address = models.CharField(max_length=255)
    # office = models.CharField(max_length=255)
    # web_address = models.URLField(
    #     max_length=200,
    #     blank=True,
    #     null=True
    # )

    # def __str__(self):
    #     return self.name
