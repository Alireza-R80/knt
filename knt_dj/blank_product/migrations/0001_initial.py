# Generated by Django 4.1.5 on 2023-01-30 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlankProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('is_available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BlankProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BlankProp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blank_props', to='blank_product.blankproducttype')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BlankPropValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10)),
                ('blank_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blank_prop_values', to='blank_product.blankproduct')),
                ('blank_prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blank_prop_values', to='blank_product.blankprop')),
            ],
        ),
        migrations.CreateModel(
            name='BlankProductSampleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=100)),
                ('blank_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blank_product_sample_images', to='blank_product.blankproduct')),
            ],
        ),
        migrations.CreateModel(
            name='BlankProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=100)),
                ('is_preview', models.BooleanField()),
                ('blank_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blank_product_images', to='blank_product.blankproduct')),
            ],
        ),
        migrations.AddField(
            model_name='blankproduct',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blank_products', to='blank_product.category'),
        ),
        migrations.AddField(
            model_name='blankproduct',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blank_products', to='blank_product.blankproducttype'),
        ),
    ]
