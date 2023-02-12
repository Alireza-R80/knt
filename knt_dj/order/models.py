from django.db import models
from account.models import *
from product.models import Product


class Order(models.Model):
    STATUS = (('PAD', 'پرداخت شده'),
              ('PRP', 'در حال آماده سازی'),
              ('PST', 'در حال ارسال'),
              ('DLV', 'تحویل داده شده'),
              ('CON', 'تایید شده'),
              ('REJ', 'رد شده'))
    customer = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='userOrders')
    product = models.ManyToManyField(Product, related_name='orders')
    provider = models.ForeignKey(PrintProvider, on_delete=models.CASCADE, related_name='providerOrders')
    address = models.CharField(max_length=300)
    status = models.CharField(choices=STATUS, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    tracking_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user} - {self.status}'
