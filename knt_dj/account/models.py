from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractBaseUser):
    phone_number = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_designer = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Designer(Customer):
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

    def __str__(self):
        return f'{self.designer} - {self.store_name}'


class PrintProvider(AbstractBaseUser):
    phone_number = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


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

    def __str__(self):
        return f'{self.print_provider} - {self.state}'


class Address(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    detail = models.TextField(max_length=500)
    post_code = models.IntegerField()
    phone_number = models.CharField(max_length=200)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.state}'
