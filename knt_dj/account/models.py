from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from utils.models import *


class UserManager(BaseUserManager):

    def create_user(self, phone_number, is_active=True, is_staff=False, password=None):
        if not password:
            raise ValueError('password is required')
        if not phone_number:
            raise ValueError('phone_number is required')
        user_obj = self.model(
            phone_number=phone_number
        )
        user_obj.password = make_password(password)
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, phone_number, password=None, ):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Customer(AbstractUser):
    roles = (('CUS', 'customer'),
             ('DES', 'designer'),
             ('PRP', 'printProvider'),
             ('ADM', 'admin'))
    val = RegexValidator(regex=r'^(09)\d{9}$')
    phone_number = models.CharField(unique=True, validators=[val], max_length=30)
    username = None
    modified_at = models.DateTimeField(auto_now_add=True, null=True)
    role = models.CharField(choices=roles, max_length=30, default='CUS')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table = 'customer'


class Designer(models.Model):
    parent_user = models.OneToOneField(Customer, related_name='designer', on_delete=models.CASCADE)
    card_number = models.CharField(max_length=200)
    is_premium = models.BooleanField(default=False)
    balance = models.FloatField(default=0)
    upgraded_at = models.DateTimeField(auto_now_add=True, null=True)


class Store(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE, related_name="stores")
    store_name = models.CharField(max_length=100)
    store_avatar = models.ImageField(
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
    num_products = models.IntegerField()
    num_sold = models.IntegerField()

    def __str__(self):
        return self.store_name


class PrintProvider(AbstractUser):
    val = RegexValidator(regex=r'^(09)\d{9}$')
    phone_number = models.CharField(max_length=11, unique=True, validators=[val])
    full_name = models.CharField(max_length=50)
    rate = models.IntegerField(default=0)
    role = models.CharField(default='PRP', max_length=10)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Print Provider'
        verbose_name_plural = 'Print Providers'
        db_table = 'print_provider'


class PrintProviderAddress(models.Model):
    print_provider = models.ForeignKey(
        PrintProvider,
        on_delete=models.CASCADE,
        related_name='print_provider_addresses')
    state = models.ForeignKey(State, related_name='print_provider_address', on_delete=models.RESTRICT)
    city = models.ForeignKey(City, related_name='print_provider_address', on_delete=models.RESTRICT)
    detail = models.TextField(max_length=500)
    post_code = models.IntegerField()
    phone_number = models.CharField(max_length=200)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.print_provider} - {self.state}'


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    state = models.ForeignKey(State, related_name='address', on_delete=models.RESTRICT)
    city = models.ForeignKey(City, related_name='address', on_delete=models.RESTRICT)
    detail = models.TextField(max_length=500)
    post_code = models.IntegerField()
    phone_number = models.CharField(max_length=200)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.state}'
