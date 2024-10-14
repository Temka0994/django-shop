from django.db import models


class ProductType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100, verbose_name='Тип товару')

    class Meta:
        verbose_name = 'Тип товару'
        verbose_name_plural = 'Тип товару'

    def __str__(self):
        return self.type_name


class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    manufacturer_name = models.CharField(max_length=100, verbose_name='Виробник')

    class Meta:
        verbose_name = 'Виробник'
        verbose_name_plural = 'Виробник'

    def __str__(self):
        return self.manufacturer_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=250, verbose_name='Товар')
    product_photo = models.CharField(max_length=250, verbose_name='Посилання на фото')
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Виробник')
    type_id = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='Тип товару')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    about = models.TextField(verbose_name='Опис')
    slug = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

    def __str__(self):
        return self.product_name


class Storage(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name='Кількість')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'

    def __str__(self):
        return f'{self.product.product_name} - {self.count}'
