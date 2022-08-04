from django.urls.base import reverse_lazy
from django.shortcuts import render, get_object_or_404
from apps.products.models import *
from apps.products.forms import *
from django.views import generic


class ProductIndexView(generic.ListView):
    queryset = Product.objects.all()
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'products'


class ProductCreateView(generic.CreateView):
    form_class = ProductForm
    success_url = reverse_lazy('index_product')
    template_name = 'products/create.html'

    # def get_initial(self):
    #     product = get_object_or_404(Product, pk=self.kwargs['pk'])
    #     self.initial.update({
    #         'user': self.request.user.id,
    #         'price': product.price,
    #         'description': product.pk,
    #         'quantity': product.quantity,
    #         'title': product.quantity,
    #         'product': product.pk
    #     })
    #     return super(ProductCreateView,self).get_initial()


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('index_product')
    template_name = 'products/delete.html'


class ProductUpdateView(generic.UpdateView):
    form_class = ProductForm
    queryset = Product.objects.all()

    success_url = reverse_lazy('index_product')
    template_name = 'products/update.html'


# class PhotoProductCreateView(generic.CreateView):
#     form_class = ProductImageForm
#
#     success_url = reverse_lazy('index_product')
#     template_name = 'products/creating.html'
# def product(request,id):
#     print(id)
#     product = Product.objects.get(pk=id)
#     return render(request, 'include/cart_form.html', {"product": product})
#
# def add_to_cart(request):
#     product = Product.objects.get(pk=request.POST['product_id'])
#     b = Basket
#     b.user = request.POST['username']
#     b.title = request.POST['title']
#     b.price = request.POST['price']
#     b.quantity = request.POST['quantity']
#     b.product = product
#     b.save()
#     return render(request,'include/cart_form.html',{"product":product})