import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


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

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_host(self,email,password):
        user = self.create_user(email,password=password)
        user.host = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def create_staff(self,email,password):
        user = self.create_user(email,password=password)
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email of username"""
    user_id = models.UUIDField(unique=True, default=uuid.uuid4)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=False, verbose_name='first name')
    last_name = models.CharField(max_length=255, blank=False, verbose_name='last name')
    host = models.BooleanField(default=False)
    interests = models.CharField(max_length=2, choices=MY_INTERESTS)
    admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="user/images", null=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return "{} {}".format(self.first_name, self.last_name)
