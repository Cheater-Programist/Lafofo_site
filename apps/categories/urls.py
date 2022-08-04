from apps.categories.views import *
from django.urls import path
from django.utils.regex_helper import normalize


urlpatterns = [
    path('', CategoryIndexView.as_view(), name='index_category'),
    path('detail/<str:slug>/', CategoryDetailView.as_view(), name='detail_category'),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'), 
    path('create/', CategoryCreateView.as_view(), name='create_category'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
]