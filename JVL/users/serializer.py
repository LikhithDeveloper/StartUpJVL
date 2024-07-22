from rest_framework import serializers
from .models import *

# class ReviewSerializer(serializers.ModelSerializer):
#     product = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all())
#     consumer = serializers.PrimaryKeyRelatedField(queryset = Consumer.objects.all())
#     class Meta:
#         model = Review
#         fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    # rating = serializers.ReadOnlyField()
    # num_reviews = serializers.ReadOnlyField()
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
#         depth = 1

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = '__all__'
        depth = 1

# class SubCategorySerializer(serializers.ModelSerializer):
#     # category = CategorySerializer()       # if we give this we should give all fields
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())      # for this we can give only id
#     # category = serializers.SlugRelatedField(      # for this we have to select what we should give
#     #     slug_field='category_id', 
#     #     queryset=Category.objects.all()
#     # )
#     class Meta:
#         model = SubCategory
#         fields = '__all__'
#         depth = 1
    


class ProductSerializer(serializers.ModelSerializer):
    consumer = serializers.PrimaryKeyRelatedField(queryset = Consumer.objects.all())
    sub_category = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all())
    # consumer = serializers.SlugRelatedField(slug_field='consumer_id',queryset = Consumer.objects.all())
    # sub_category = serializers.SlugRelatedField(slug_field='sub_cat_id',queryset = SubCategory.objects.all())

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset = Profile.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all())
    class Meta:
        model = Order
        fields = '__all__'
        depth = 1


class AddToCartSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset = Profile.objects.all())
    product_cart = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all())
    class Meta:
        model = AddToCart
        fields = '__all__'
        depth = 1


class WishListSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset = Profile.objects.all())
    product_cart = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all())
    class Meta:
        model = WishList
        fields = '__all__'
        depth = 1

