from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Category(MPTTModel):
    name = models.CharField(verbose_name='Category Name', max_length=255, unique=True)
    slug = models.SlugField(verbose_name='Category safe URL', max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class BlankProductType(models.Model):
    name = models.CharField(max_length=20)
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

    def __str__(self):
        return self.name


class BlankProductProp(models.Model):
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


class BlankProductPropValue(models.Model):
    blank_product = models.ForeignKey(BlankProduct, related_name='blank_prop_values', on_delete=models.CASCADE)
    blank_prop = models.ForeignKey(BlankProductProp, related_name='blank_prop_values', on_delete=models.CASCADE)
    value = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.blank_product} - {self.blank_prop}'


class BlankProductImage(models.Model):
    blank_product = models.ForeignKey(BlankProduct, related_name='blank_product_images', on_delete=models.CASCADE)
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
    is_preview = models.BooleanField()
    #
    # def __str__(self):
    #     return self.blank_product


class BlankProductSampleImage(models.Model):
    blank_product = models.ForeignKey(BlankProduct, related_name='blank_product_sample_images',
                                      on_delete=models.CASCADE)
    src = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.blank_product

