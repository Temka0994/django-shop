from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product


class OrderList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Кошик'
        verbose_name_plural = 'Кошик'

    def __str__(self):
        return f'Order {self.pk} - {self.product.product_name} ({self.count} шт.)'
