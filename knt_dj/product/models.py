from django.db import models

from blank_product.models import BlankProduct, BlankProductType


class Product(models.Model):
    STATUS = (('DES', 'طراحی شده'),
              ('CON', 'تایید شده'),
              ('REJ', 'رد شده'))
    name = models.CharField(max_length=20)
    description = models.TextField()
    blank_product = models.ForeignKey(BlankProduct, on_delete=models.CASCADE, related_name='product')
    # needs to be modified (Foreign Key: to designer and provider)
    designer_id = models.IntegerField()
    provider_id = models.IntegerField()
    design_src = models.CharField(max_length=60)
    sample_src = models.CharField(max_length=60)
    discount_percent = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=15)
    is_available = models.BooleanField(default=False)
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    src = models.CharField(max_length=60)
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


class ProductProviderProp(models.Model):
    blank_product = models.ForeignKey(BlankProduct, on_delete=models.CASCADE, related_name='ppp')
    # needs to be modified
    provider_id = models.IntegerField()
    prep_time = models.CharField(max_length=20)


class ProductProviderDetail(models.Model):
    product_provider_prop = models.ForeignKey(ProductProviderProp, on_delete=models.CASCADE, related_name='ppd')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name='ppd', null=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, related_name='ppd', null=True)
    price = models.FloatField()
