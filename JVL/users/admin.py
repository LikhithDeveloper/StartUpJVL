from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Consumer)
admin.site.register(SubCategory)
admin.site.register(Product)
# admin.site.register(Review)
admin.site.register(Order)
admin.site.register(AddToCart)
admin.site.register(WishList)

