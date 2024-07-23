# panel/models.py

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Request(models.Model):
    request_id = models.CharField(max_length=20, unique=True, blank=True)
    consumer_name = models.CharField(max_length=50)
    consumer_number = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    brand_name = models.CharField(max_length=50, unique=True)
    is_accepted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.request_id:
            last_consumer = Request.objects.all().order_by('id').last()
            if last_consumer:
                last_id = int(last_consumer.request_id.replace('REQUEST', ''))
                new_id = f'REQUEST{last_id + 1:02d}'
            else:
                new_id = 'REQUEST01'
            self.request_id = new_id
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.consumer_name

@receiver(post_save, sender=Request)
def create_consumer(sender, instance, created, **kwargs):
    if instance.is_accepted:
        from users.models import Consumer
        if not Consumer.objects.filter(consumer_name=instance.consumer_name).exists():
            Consumer.objects.create(
                consumer_name=instance.consumer_name,
                consumer_number=instance.consumer_number,
                email=instance.email,
                brand_name=instance.brand_name
            )

# Category model
class Category(models.Model):
    category_id = models.CharField(max_length=20, unique=True, blank=True)
    category_name = models.CharField(max_length=50, unique=True)
    category_description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.category_id:
            last_category = Category.objects.all().order_by('id').last()
            if last_category:
                last_id = int(last_category.category_id.replace('CATEGORY', ''))
                new_id = f'CATEGORY{last_id + 1:02d}'
            else:
                new_id = 'CATEGORY01'
            self.category_id = new_id
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name

# SubCategory model
class SubCategory(models.Model):
    sub_cat_id = models.CharField(max_length=20, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_cat_name = models.CharField(max_length=50, unique=True)
    sub_cat_description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.sub_cat_id:
            last_sub_cat = SubCategory.objects.all().order_by('id').last()
            if last_sub_cat:
                last_id = int(last_sub_cat.sub_cat_id.replace('SUB_CAT', ''))
                new_id = f'SUB_CAT{last_id + 1:02d}'
            else:
                new_id = 'SUB_CAT01'
            self.sub_cat_id = new_id
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.sub_cat_name

class ConsumerPanel(models.Model):
    consumer = models.ForeignKey('users.Consumer', on_delete=models.CASCADE)
    order_id = models.CharField(max_length=20)
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=100)
    coustemer_name = models.CharField(max_length=30)
    coustomer_mobile_number = models.CharField(max_length=13)
    coustemer_email = models.EmailField()
    coustomer_address = models.TextField()
