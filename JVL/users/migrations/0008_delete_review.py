# Generated by Django 5.0.7 on 2024-07-22 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_subcategory_category_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]