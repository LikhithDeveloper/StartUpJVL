from django.db import models
from panel.models import Request,Category,SubCategory,ConsumerPanel
from django.db.models.signals import post_save
from django.dispatch import receiver

# Profile model
class Profile(models.Model):
    custom_id = models.CharField(max_length=20, unique=True, blank=True,null=True)
    name = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=13,unique=True)
    email = models.EmailField(max_length=30, null=True, blank=True,unique=True)
    address = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.custom_id:
            last_profile = Profile.objects.all().order_by('id').last()
            if last_profile:
                last_id = int(last_profile.custom_id.replace('PROFILE', ''))
                new_id = f'PROFILE{last_id + 1:02d}'
            else:
                new_id = 'PROFILE01'
            self.custom_id = new_id
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name




# Consumer model
class Consumer(models.Model):
    consumer_id = models.CharField(max_length=20, unique=True, blank=True)
    consumer_name = models.CharField(max_length=50)
    consumer_number = models.CharField(max_length=12,unique=True)
    email = models.EmailField(unique=True)
    brand_name = models.CharField(max_length=50,unique=True)

    def save(self, *args, **kwargs):
        if not self.consumer_id:
            last_consumer = Consumer.objects.all().order_by('id').last()
            if last_consumer:
                last_id = int(last_consumer.consumer_id.replace('CONSUMER', ''))
                new_id = f'CONSUMER{last_id + 1:02d}'
            else:
                new_id = 'CONSUMER01'
            self.consumer_id = new_id
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.consumer_name


# Product model
from django.db.models import Avg

class Product(models.Model):
    product_id = models.CharField(max_length=20, unique=True, blank=True)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='images/',null=True,blank=True)
    price = models.IntegerField()
    count_stock = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.product_id:
            last_product = Product.objects.all().order_by('id').last()
            if last_product:
                last_id = int(last_product.product_id.replace('PRODUCT', ''))
                new_id = f'PRODUCT{last_id + 1:02d}'
            else:
                new_id = 'PRODUCT01'
            self.product_id = new_id
        super().save(*args, **kwargs)

    # @property
    # def rating(self):
    #     reviews = self.reviews.all()
    #     if reviews.exists():
    #         return reviews.aggregate(Avg('rating'))['rating__avg']
    #     return 0.0

    # @property
    # def num_reviews(self):
    #     return self.reviews.count()

    def __str__(self):
        return self.product_name

    
# review and rating

# class Review(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
#     consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
#     rating = models.DecimalField(max_digits=2, decimal_places=1)
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Review for {self.product.product_name} by {self.consumer}'



# Order model
class Order(models.Model):
    order_id = models.CharField(max_length=20, unique=True,blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.order_id:
            last_profile = Order.objects.all().order_by('id').last()
            if last_profile:
                last_id = int(last_profile.order_id.replace('ORDER', ''))
                new_id = f'ORDER{last_id + 1:02d}'
            else:
                new_id = 'ORDER01'
            self.order_id = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id

@receiver(post_save, sender=Order)
def create_consumerPanel(sender, instance, created, **kwargs):
    from users.models import ConsumerPanel
    if created:
        ConsumerPanel.objects.create(
            consumer = instance.product.consumer,
            order_id=instance.order_id,
            product_id=instance.product.product_id,
            product_name=instance.product.product_name,
            coustemer_name=instance.profile.name,  
            coustomer_mobile_number=instance.profile.mobile_no,  
            coustemer_email=instance.profile.email,  
            coustomer_address=instance.profile.address  
        )

# AddToCart model
class AddToCart(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    product_cart = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.profile.name
    
# Whishlist model
class WishList(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    product_cart = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.profile.name
    