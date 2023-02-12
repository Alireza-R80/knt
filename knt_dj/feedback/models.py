from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from product.models import Product
from account.models import Customer


# Create your models here.
class ProductRate(models.Model):
    product = models.ForeignKey(Product, related_name="productRate", on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, related_name="productRate", on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'product'),)

    def __str__(self):
        return f'{self.user} - {self.product}'


class ProductReport(models.Model):
    STATUS = (('DEL', 'تحویل داده شده'),
              ('CHK', 'برسی شده'),
              ('REJ', 'رد شده'),
              ('COF', 'رسیدگی شده'))  # TODO
    user = models.ForeignKey(Customer, related_name="report", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="report", on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=20)  # TODO
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.product} - {self.status}'


class ProductComment(models.Model):
    user = models.ForeignKey(Customer, related_name="comments", on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    text = models.TextField()
    like = models.IntegerField()
    dissLike = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.title}'