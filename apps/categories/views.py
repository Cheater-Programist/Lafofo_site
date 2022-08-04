from django.urls.base import reverse_lazy
from apps.categories.models import Category
from apps.categories.forms import CategoryForm
from django.views import generic



class CategoryIndexView(generic.ListView):
    queryset = Category.objects.all()
    model = Category
    template_name = 'category/index.html'
    context_object_name = 'categories'

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'category/detail.html'
    context_object_name = 'category'

class CategoryCreateView(generic.CreateView):
    form_class = CategoryForm
    success_url = reverse_lazy('index_category')
    template_name = 'category/create.html'
    
class CategoryDeleteView(generic.DeleteView):
    model = Category
    success_url = reverse_lazy('index_category')
    template_name = 'category/delete.html'


class CategoryUpdateView(generic.UpdateView):

    form_class = CategoryForm
    queryset = Category.objects.all()
    
    success_url = reverse_lazy('index_category')
    template_name = 'category/update.html'