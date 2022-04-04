from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.translation import gettext as _

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, **extra_fields):

        if not username:
            raise ValueError(_('The name must be set'))

        user = self.model(username=username, **extra_fields)
        user.set_password(extra_fields['password'])
        user.save()
        return user

    def create_superuser(self, username, **extra_fields):

        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username=username, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Name'), max_length=50, unique=True)
    # user_phone = models.CharField(_('Phone Number'), max_length=20,
    #                               unique=True, default=None, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


def __str__(self):
    return f'{self.username}'


# Karkasni

class Karkas(models.Model):
    image = models.ImageField(upload_to='images/')
    latestCost = models.CharField(max_length=200)
    nowCost = models.CharField(max_length=200)
    howMuch = models.CharField(max_length=200)
    frame = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    deep = models.CharField(max_length=200)

    def __str__(self):
        return self.image


class Naduvnie(models.Model):
    image = models.ImageField(upload_to='images/')
    latestCost = models.CharField(max_length=200)
    nowCost = models.CharField(max_length=200)
    howMuch = models.CharField(max_length=200)
    frame = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    deep = models.CharField(max_length=200)

    def __str__(self):
        return self.image


class Zakaz(models.Model):
    client_name = models.CharField(max_length=200)
    telNumber = models.CharField(max_length=200)
    poolFrame = models.CharField(max_length=200)
    money = models.CharField(max_length=200)

    def __str__(self):
        return self.client_name



class Kansultatsi(models.Model):
    name_Klent = models.CharField(max_length=300)
    telNumberKlent = models.CharField(max_length=300)

    def __str__(self):
        return self.name_Klent
