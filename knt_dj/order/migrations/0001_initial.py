# Generated by Django 4.1.5 on 2023-02-07 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('status', models.CharField(choices=[('PAD', 'پرداخت شده'), ('PRP', 'در حال آماده سازی'), ('PST', 'در حال ارسال'), ('DLV', 'تحویل داده شده'), ('CON', 'تایید شده'), ('REJ', 'رد شده')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField()),
                ('tracking_code', models.CharField(max_length=20)),
                ('product', models.ManyToManyField(related_name='orders', to='product.product')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='account.printprovider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
