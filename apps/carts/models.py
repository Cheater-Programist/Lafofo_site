from django.db import models
from django.contrib.auth import get_user_model
from apps.products.models import Product
from django.db.models.signals import m2m_changed,pre_save
from decimal import Decimal

User = get_user_model()

# class Basket(models.Model):
#     user = models.ForeignKey(
#             User,on_delete=models.SET_NULL,related_name='cart_user',blank=True,null=True
#         )
#     product = models.ManyToManyField(Product, related_name='cart_product', blank=True)
#     title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
#     price = models.IntegerField(verbose_name='цена')

#
class CartManager(models.Manager):
    def get_or_new(self,request):
        new = False
        cart_id = request.session.get('cart_id',None)
        qs = self.get_queryset().filter(id=cart_id,status ='op')
        if qs.count() == 1:
            cart_obj = qs.first()
            if request.user.is_authenticated and not cart_obj.user:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = self.new(user=request.user)
            new=True
            request.session['cart_id'] = cart_obj.id
            print('Cart created')
        return cart_obj,new

    def new(self,user=None):
        user_obj = None
        if user and user.is_authenticated:
            user_obj = user
        return self.model.object.create(user=user_obj)


class Cart(models.Model):
    OPENED = 'op'
    CLOSED = 'cl'
    STATUS_CHOICES = (
        (OPENED,'Opened'),
        (CLOSED, 'Closed'),
    )
    user = models.ForeignKey(
        User,on_delete=models.SET_NULL,related_name='user_cart',blank=True,null=True
    )
    products = models.ManyToManyField(Product,related_name='product_cart',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    subtotal = models.DecimalField(max_digits=20,decimal_places=2,default=0)
    total = models.DecimalField(max_digits=20,decimal_places=2,default=0)
    status = models.CharField(max_length=2,choices=STATUS_CHOICES,default=OPENED)

    object = CartManager()

    def str(self):
        return f'{self.id}'


def cart_m2m_changed_receiver(sender,instance,action,*args,**kwargs):
    if action in ['post_add','post_remove','post_clear']:
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.prices
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(
    cart_m2m_changed_receiver,
    sender = Cart.products.through
)


def total_price_pre_save_receiver(sender,instance,*args,**kwargs):
    if instance.subtotal != 0:
        instance.total = Decimal(instance.subtotal) * Decimal(1.08)
    else:
        instance.total = 0


pre_save.connect(
    total_price_pre_save_receiver,
    sender = Cart
)