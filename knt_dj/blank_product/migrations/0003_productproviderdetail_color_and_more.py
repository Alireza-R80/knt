# Generated by Django 4.1.5 on 2023-02-08 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blank_product', '0002_productproviderdetail_productproviderprop'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productproviderdetail',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ppd', to='utils.color'),
        ),
        migrations.AddField(
            model_name='productproviderdetail',
            name='product_provider_prop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ppd', to='blank_product.productproviderprop'),
        ),
        migrations.AddField(
            model_name='productproviderdetail',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ppd', to='utils.size'),
        ),
    ]
