# Generated by Django 4.1.5 on 2023-02-07 19:39

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


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
            name='BlankProductProp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BlankProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(default='images/default.png', upload_to='images/', verbose_name='image')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Alternative text')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Category safe URL')),
                ('is_active', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blank_product.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
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
            name='BlankProductPropValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10)),
                ('blank_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blank_prop_values', to='blank_product.blankproduct')),
                ('blank_prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blank_prop_values', to='blank_product.blankproductprop')),
            ],
        ),
        migrations.AddField(
            model_name='blankproductprop',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blank_props', to='blank_product.blankproducttype'),
        ),
        migrations.CreateModel(
            name='BlankProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.png', upload_to='images/', verbose_name='image')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Alternative text')),
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
