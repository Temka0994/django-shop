from .models import Product, ProductType, Manufacturer
from django.views import generic


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'catalog/catalog.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        product_type = self.request.GET.get('type_id')
        manufacturer = self.request.GET.get('manufacturer_id')
        order_by = self.request.GET.get('order_by', 'default')

        if product_type:
            queryset = queryset.filter(type_id=product_type)
        if manufacturer:
            queryset = queryset.filter(manufacturer_id=manufacturer)

        if order_by == '-price':
            queryset = queryset.order_by('-price')
        elif order_by == 'price':
            queryset = queryset.order_by('price')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['selected_type'] = self.request.GET.get('type_id', '')
        context['selected_manufacturer'] = self.request.GET.get('manufacturer_id', '')
        context['selected_order_by'] = self.request.GET.get('order_by', 'default')
        context['product_types'] = ProductType.objects.all()
        context['manufacturers'] = Manufacturer.objects.all()

        return context


class ProductDetailView(generic.DetailView):
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    template_name = 'catalog/product_details.html'
