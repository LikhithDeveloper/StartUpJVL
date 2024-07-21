# Generated by Django 5.0.7 on 2024-07-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=13)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]