# Generated by Django 5.0.7 on 2024-07-27 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
    ]
