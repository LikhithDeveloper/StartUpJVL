from rest_framework import serializers
from .models import *
from users.models import*

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        depth = 1

class SubCategorySerializer(serializers.ModelSerializer):
    # category = CategorySerializer()       # if we give this we should give all fields
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())      # for this we can give only id
    # category = serializers.SlugRelatedField(      # for this we have to select what we should give
    #     slug_field='category_id', 
    #     queryset=Category.objects.all()
    # )
    class Meta:
        model = SubCategory
        fields = '__all__'
        depth = 1
    