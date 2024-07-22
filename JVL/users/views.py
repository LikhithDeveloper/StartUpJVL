from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *


# profiles apis
@api_view(['POST','GET','PUT','PATCH','DELETE'])

def profile(request):
    if request.method == 'POST':
        data = request.data
        serializer = ProfileSerializer(data = data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'GET':
        objs = Profile.objects.all()
        serializer = ProfileSerializer(objs,many = True)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Profile.objects.get(id = data['id'])
        serializer = ProfileSerializer(obj,data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        print(data)
        obj = Profile.objects.get(id = data['id'])
        serializer = ProfileSerializer(obj,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Profile.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'Profile deleted'})



# category api

@api_view(['POST','GET','PUT','PATCH','DELETE'])

def category(request):
    if request.method == 'POST':
        data = request.data
        serializer = CategorySerializer(data = data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'GET':
        objs = Category.objects.all()
        serializer = CategorySerializer(objs ,many = True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Category.objects.get(id = data['id'])
        serializer = CategorySerializer(obj,data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        print(data)
        obj = Category.objects.get(id = data['id'])
        serializer = CategorySerializer(obj,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Category.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'Profile deleted'})
    

# consumer api

@api_view(['POST','GET','PUT','PATCH','DELETE'])

def consumer(request):
    if request.method == 'POST':
        data = request.data
        serializer = ConsumerSerializer(data = data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'GET':
        objs = Consumer.objects.all()
        serializer = ConsumerSerializer(objs ,many = True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Consumer.objects.get(id = data['id'])
        serializer = ConsumerSerializer(obj,data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        print(data)
        obj = Consumer.objects.get(id = data['id'])
        serializer = ConsumerSerializer(obj,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Consumer.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'Profile deleted'})
    

# sub category api

@api_view(['POST','GET','PUT','PATCH','DELETE'])

def subcategory(request):
    if request.method == 'POST':
        data = request.data
        serializer = SubCategorySerializer(data = data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'GET':
        objs = SubCategory.objects.all()
        serializer = SubCategorySerializer(objs ,many = True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = SubCategory.objects.get(id = data['id'])
        serializer = SubCategorySerializer(obj,data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        print(data)
        obj = SubCategory.objects.get(id = data['id'])
        serializer = SubCategorySerializer(obj,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = SubCategory.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'Profile deleted'})
    
# Product api

@api_view(['POST','GET','PUT','PATCH','DELETE'])

def product(request):
    if request.method == 'POST':
        data = request.data
        serializer = ProductSerializer(data = data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'GET':
        objs = Product.objects.all()
        serializer = ProductSerializer(objs ,many = True)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Product.objects.get(id = data['id'])
        serializer = ProductSerializer(obj,data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        print(data)
        obj = Product.objects.get(id = data['id'])
        serializer = ProductSerializer(obj,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Product.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'Profile deleted'})
    


# Orders api

@api_view(['POST','GET','PUT','PATCH','DELETE'])

def order(request):
    if request.method == 'POST':
        data = request.data
        serializer = OrderSerializer(data = data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'GET':
        objs = Order.objects.all()
        serializer = OrderSerializer(objs ,many = True)
        return Response(serializer.data)
        
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Order.objects.get(id = data['id'])
        serializer = OrderSerializer(obj,data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        print(data)
        obj = Order.objects.get(id = data['id'])
        serializer = OrderSerializer(obj,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Order.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'Profile deleted'})
    

# addtocart api

@api_view(['POST','GET'])

def addtocart(request):
    if request.method == 'POST':
        data = request.data
        serializer = AddToCartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'GET':
        objs = AddToCart.objects.all()
        serializer = AddToCartSerializer(objs,many = True)
        return Response(serializer.data)
    

# wishlist api

@api_view(['POST','GET'])

def wishList(request):
    if request.method == 'POST':
        data = request.data
        serializer = WishListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'GET':
        objs = WishList.objects.all()
        serializer = WishListSerializer(objs,many = True)
        return Response(serializer.data)