from apps.products.views import *
from django.urls import path
from django.utils.regex_helper import normalize


urlpatterns = [
    path('', ProductIndexView.as_view(), name='index_product'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'), 
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    # path('add/<int:id>/', add_to_cart, name='add_to_cart'),
    # path('product/<int:id>', product, name='product')
]