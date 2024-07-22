from django.db import models
from users.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Request(models.Model):
    request_id = models.CharField(max_length=20, unique=True, blank=True)
    consumer_name = models.CharField(max_length=50)
    consumer_number = models.CharField(max_length=12)
    email = models.EmailField()
    brand_name = models.CharField(max_length=50)
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
    if instance.is_accepted and not Consumer.objects.filter(consumer_name=instance.consumer_name).exists():
        Consumer.objects.create(
            consumer_name=instance.consumer_name,
            consumer_number=instance.consumer_number,
            email=instance.email,
            brand_name=instance.brand_name
        )
