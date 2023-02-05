from django.db import models
from account.models import *
from blank_product.models import BlankProduct, BlankProductType


class Product(models.Model):
    STATUS = (('DES', 'طراحی شده'),
              ('CON', 'تایید شده'),
              ('REJ', 'رد شده'))
    name = models.CharField(max_length=20)
    description = models.TextField()
    blank_product = models.ForeignKey(BlankProduct, on_delete=models.CASCADE, related_name='product')
    designer = models.ForeignKey(Designer, on_delete=models.SET_NULL, null=True, related_name='products')
    provider = models.ForeignKey(PrintProvider, on_delete=models.SET_NULL, null=True, related_name='products')
    design_img = models.ImageField(
        verbose_name='image',
        upload_to='images/',
        default='images/default.png'
    )
    sample_img = models.ImageField(
        verbose_name='image',
        upload_to='images/',
        default='images/default.png'
    )
    discount_percent = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=15)
    is_available = models.BooleanField(default=False)
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(
        verbose_name='image',
        upload_to='images/',
        default='images/default.png'
    )
    alt_text = models.CharField(
        verbose_name='Alternative text',
        max_length=255,
        null=True,
        blank=True,
    )
    is_preview = models.BooleanField(default=False)


class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Size(models.Model):
    type = models.ForeignKey(BlankProductType, on_delete=models.CASCADE, related_name='sizes')
    unit = models.CharField(max_length=10)


# to see if product with color n exists with size m and how much is the price for each combination
class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_details')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name='product_details', null=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, related_name='product_details', null=True)
    price = models.FloatField()

    def __str__(self):
        return self.product


class ProductProviderProp(models.Model):
    blank_product = models.ForeignKey(BlankProduct, on_delete=models.CASCADE, related_name='ppp')
    provider = models.ForeignKey(
        PrintProvider,
        on_delete=models.CASCADE,
        null=True,
        related_name='product_provider_prop')
    prep_time = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.blank_product} - {self.provider}'


class ProductProviderDetail(models.Model):
    product_provider_prop = models.ForeignKey(ProductProviderProp, on_delete=models.CASCADE, related_name='ppd')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name='ppd', null=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, related_name='ppd', null=True)
    price = models.FloatField()

    def __str__(self):
        return self.product_provider_prop
