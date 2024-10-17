from .models import Product
from django.views import generic


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'catalog/catalog.html'
    paginate_by = 9


class ProductDetailView(generic.DetailView):
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    template_name = 'catalog/product_details.html'

