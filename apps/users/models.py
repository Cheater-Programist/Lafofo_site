from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.slug_generator import unique_slug_generators
from django.db.models.signals import pre_save

class User(AbstractUser):
    GENDER_CHOICES = (  
        ('m', 'male'),
        ('f', 'female'),
    )

    username = models.CharField(max_length=255, unique=True)
    profile = models.ImageField(
        upload_to = 'profiles', blank = True, null =True
    )
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=255
    )
    slug = models.SlugField(blank=True, null=True)

# def slug_pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generators(instance)
#
#
# pre_save.connect(slug_pre_save_receiver, sender=User)