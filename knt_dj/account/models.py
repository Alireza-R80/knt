from django.contrib.auth.models import AbstractUser
from django.db import models


class Costumer(AbstractUser, models.Model):
    is_designer = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now_add=True)


class Designer(Costumer, models.Model):
    card_number = models.CharField(max_length=200)
    is_premium = models.BooleanField(default=False)
    balance = models.FloatField()
    upgraded_at = models.DateTimeField(auto_now_add=True)


class Store(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE, related_name="stores")
    store_name = models.CharField(max_length=100)
    store_avatar = models.CharField(max_length=200)
    num_products = models.IntegerField()
    num_sold = models.IntegerField()


class PrintProvider(Costumer, models.Model):
    rate = models.IntegerField(default=0)


class PrintProviderAddress(models.Model):
    print_provider = models.ForeignKey(
        PrintProvider,
        on_delete=models.CASCADE,
        related_name='print_provider_addresses')
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    detail = models.TextField(max_length=500)
    post_code = models.IntegerField()
    phone_number = models.CharField(max_length=200)
    is_default = models.BooleanField(default=False)


class Address(models.Model):
    user = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name='addresses')
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    detail = models.TextField(max_length=500)
    post_code = models.IntegerField()
    phone_number = models.CharField(max_length=200)
    is_default = models.BooleanField(default=False)
