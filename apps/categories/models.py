from django.db.models.signals import pre_save
from utils.slug_generator import unique_slug_generators
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255,verbose_name="Название")
    parent = models.ForeignKey('self',on_delete=models.CASCADE, related_name='under_category',blank=True,null=True,verbose_name="Родительский")
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self) -> str:
        return self.title

def slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)

pre_save.connect(slug_pre_save_receiver, sender=Category)