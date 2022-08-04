
from django.db import models

from utils.slug_generator import unique_slug_generators
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from apps.categories.models import Category

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Пользователь", related_name='product_user')
    image = models.ImageField(upload_to='product/', verbose_name='Картинка', blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    is_stock = models.BooleanField(default=True, db_index=True)
    slug = models.SlugField(blank=True, unique=True)
    category = models.ForeignKey(Category,verbose_name="категория", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('title',)
        index_together = (('id','slug'), )


# class ProductImage(models.Model):
#     image = models.ImageField(upload_to = 'product/',verbose_name = 'Картинка',blank = True,null = True)
#     product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_image',null=True, blank=True)
#
#     def str(self):
#         return self.product.title
# class Basket(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='cart_product', blank=True)
#     title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
#     price = models.IntegerField(verbose_name='цена')
#     quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

def slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slug_pre_save_receiver, sender=Product)