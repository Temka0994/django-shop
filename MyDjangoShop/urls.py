"""URL configuration for MyDjangoShop project."""
from django.contrib import admin
from django.urls import path
import home.views
import about.views
from catalog.views import ProductListView, ProductDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name='home'),
    path('about/', about.views.about, name="about"),
    path('catalog/', ProductListView.as_view(), name="catalog"),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name="product_details"),
] + static(settings.MEDIA_URL)
