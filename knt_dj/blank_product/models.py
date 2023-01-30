from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    # MPTT

    def __str__(self):
        return self.name


class BlankProductType(models.Model):
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BlankProp(models.Model):
    name = models.CharField(max_length=20)
    type = models.ForeignKey(BlankProductType, related_name='blank_props', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.type}'


class BlankProduct(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, related_name='blank_products', on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(BlankProductType, related_name='blank_products', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    is_available = models.BooleanField()

    def __str__(self):
        return self.title


class BlankPropValue(models.Model):
    blank_product = models.ForeignKey(BlankProduct, related_name='blank_prop_values', on_delete=models.CASCADE)
    blank_prop = models.ForeignKey(BlankProp, related_name='blank_prop_values', on_delete=models.CASCADE)
    value = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.blank_product} - {self.blank_prop}'


class BlankProductImage(models.Model):
    blank_product = models.ForeignKey(BlankProduct, related_name='blank_product_images', on_delete=models.CASCADE)
    src = models.CharField(max_length=100)
    is_preview = models.BooleanField()

    def __str__(self):
        return self.blank_product


class BlankProductSampleImage(models.Model):
    blank_product = models.ForeignKey(BlankProduct, related_name='blank_product_sample_images',
                                      on_delete=models.CASCADE)
    src = models.CharField(max_length=100)

    def __str__(self):
        return self.blank_product

