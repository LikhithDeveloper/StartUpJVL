# Generated by Django 5.0.7 on 2024-07-21 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='custom_id',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
