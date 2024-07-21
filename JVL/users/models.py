from django.db import models

# Profile model
class Profile(models.Model):
    custom_id = models.CharField(max_length=20, unique=True, blank=True,null=True)
    name = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=13)
    email = models.EmailField(max_length=30, null=True, blank=True)
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



# Category model
class Category(models.Model):
    category_id = models.CharField(max_length=20, unique=True, blank=True)
    category_name = models.CharField(max_length=50)
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

# Consumer model
class Consumer(models.Model):
    consumer_id = models.CharField(max_length=20, unique=True, blank=True)
    consumer_name = models.CharField(max_length=50)
    consumer_number = models.CharField(max_length=12)
    email = models.EmailField()
    brand_name = models.CharField(max_length=50)

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

# SubCategory model
class SubCategory(models.Model):
    sub_cat_id = models.CharField(max_length=20, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_cat_name = models.CharField(max_length=50)
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

# Product model
class Product(models.Model):
    product_id = models.CharField(max_length=20, unique=True, blank=True)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    count_stock = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    num_reviews = models.IntegerField()

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

    def __str__(self) -> str:
        return self.product_name
    


# Order model
class Order(models.Model):
    order_id = models.CharField(max_length=20, unique=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

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
    