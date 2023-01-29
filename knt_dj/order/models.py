from django.db import models
from account.models import *


class Order(models.Model):
    STATUS = (('DES', 'طراحی شده'),  # todo
              ('CON', 'تایید شده'),
              ('REJ', 'رد شده'))
    user = models.ForeignKey('Costumer', on_delete=models.CASCADE, related_name='orders')
    # product = models.ForeignKey() todo
    provider = models.ForeignKey('PrintProvider', on_delete=models.CASCADE, related_name='orders')
    # address = models.ForeignKey('Address', on_delete=models.) todo
    status = models.CharField(choices=STATUS, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    tracking_code = models.CharField(max_length=20)
