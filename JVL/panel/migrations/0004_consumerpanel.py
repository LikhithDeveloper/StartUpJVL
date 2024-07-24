# Generated by Django 5.0.7 on 2024-07-23 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_category_subcategory'),
        ('users', '0009_remove_order_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20)),
                ('product_id', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=100)),
                ('coustemer_name', models.CharField(max_length=30)),
                ('coustomer_mobile_number', models.CharField(max_length=13)),
                ('coustemer_email', models.EmailField(max_length=254)),
                ('coustomer_address', models.TextField()),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.consumer')),
            ],
        ),
    ]