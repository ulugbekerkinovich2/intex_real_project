from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.translation import gettext as _

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


def __str__(self):
    return f'{self.username}'


class Kategoriya(models.Model):
    title = models.CharField(max_length=300, verbose_name='kategoryuzRU')
    description = models.CharField(max_length=400, verbose_name='kategoryruUZ')
    CategoriyaName = models.CharField(max_length=200, default='none')

    def __str__(self):
        return self.title


class Karkas(models.Model):
    img = models.ImageField(upload_to='images/', null=False, blank=False)
    eskiNarh = models.CharField(max_length=300, null=False)
    hozirgiNarh = models.CharField(max_length=300, blank=False)
    nechtaligi = models.CharField(max_length=300, null=False)
    ramkaRu = models.CharField(max_length=200, null=False)
    razmer = models.CharField(max_length=300, null=False)
    chuqurligi = models.CharField(max_length=300, null=False)
    commentUZ = models.TextField(max_length=3000, null=False, verbose_name='commentUZ')
    commentRU = models.TextField(max_length=3000, null=False, verbose_name='commentRU')
    ramkaUz = models.CharField(max_length=20, null=False)
    kamplektatsiyARu1 = models.CharField(max_length=200, null=False, verbose_name='kamplektatsiyARu1')
    kamplektatsiyAUz = models.CharField(max_length=200, null=False, verbose_name='kamplektatsiyAUz')
    categoriya = models.CharField(max_length=200, null=False)  # agar null False bolsa toldirish majburiy boladi
    modul = models.ForeignKey(Kategoriya, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"soni: {self.nechtaligi}\nrasmi: {self.img}\n"


class Naduvnie(models.Model):
    img = models.ImageField(upload_to='images/', null=False)
    eskiNarh = models.CharField(max_length=300, null=False)
    hozirgiNarh = models.CharField(max_length=300, null=False)
    nechtaligi = models.CharField(max_length=300, null=False)  #############
    ramkaRu = models.CharField(max_length=200, null=False)
    razmer = models.CharField(max_length=300, null=False)
    chuqurligi = models.CharField(max_length=300, null=False)
    comment = models.TextField(max_length=3000, null=False)
    ramkaUz = models.CharField(max_length=20, null=False)
    kamplektatsiyARu1 = models.CharField(max_length=200, null=False, verbose_name='kamplektatsiyaRu1')
    kamplektatsiyAUz = models.CharField(max_length=200, null=False, verbose_name='kamplektatsiyaUz')
    categoriya = models.CharField(max_length=200)

    def __str__(self):
        return self.hozirgiNarh


class Customs(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=40)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Zakaz(models.Model):
    client_name = models.CharField(max_length=200)
    telNumber = models.CharField(max_length=200)
    poolFrame = models.CharField(max_length=200)
    money = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date_time = models.DateField()
    image = models.ImageField(upload_to='images/')
    active = models.BooleanField(default=False)  #########
    product_name = models.ForeignKey(Karkas, on_delete=models.CASCADE)  #######
    count = models.IntegerField(default='none')

    def __str__(self):
        return f'{self.active}'


class Kansultatsi(models.Model):
    name_Klent = models.CharField(max_length=300)
    telNumberKlent = models.CharField(max_length=300)
    date_time = models.DateField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name_Klent


class Asosiy(models.Model):
    adminTel = models.CharField(max_length=100, null=False)
    telegramLink = models.URLField(max_length=100, null=False)
    instagramLink = models.URLField(max_length=100, null=False)
    ishVaqtiRU = models.CharField(max_length=100, null=False)
    ishVaqtiUZ = models.CharField(max_length=100, null=False)
    manzilRU = models.CharField(max_length=100, null=False)
    manzilUZ = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.adminTel


@receiver(post_save, sender=Zakaz)
def sub_count(sender, instance, *args, **kwargs):
    if instance.active:
        Karkas.objects.filter(id=instance.product_name.id).update(nechtaligi=F('nechtaligi') - instance.count)
        # Karkas.objects.filter(id=instance.product.name.id).update(eskiNarh=F('eskiNarh') + instance.hozirgiNarh)
