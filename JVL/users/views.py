from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializer import *


# profiles apis
@api_view(['POST','GET','PUT','PATCH','DELETE'])
def profile(request):
    try:
        if request.method == 'POST':
            data = request.data
            serializer = ProfileSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            objs = Profile.objects.all()
            serializer = ProfileSerializer(objs, many=True)
            return Response(serializer.data)

        elif request.method == 'PATCH':
            data = request.data
            obj = Profile.objects.get(id=data['id'])
            serializer = ProfileSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':
            data = request.data
            obj = Profile.objects.get(id=data['id'])
            serializer = ProfileSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            data = request.data
            obj = Profile.objects.get(id=data['id'])
            obj.delete()
            return Response({'message': 'Profile deleted'})
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# # category api
# @api_view(['POST','GET','PUT','PATCH','DELETE'])
# def category(request):
#     try:
#         if request.method == 'POST':
#             data = request.data
#             serializer = CategorySerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         elif request.method == 'GET':
#             objs = Category.objects.all()
#             serializer = CategorySerializer(objs, many=True)
#             return Response(serializer.data)

#         elif request.method == 'PATCH':
#             data = request.data
#             obj = Category.objects.get(id=data['id'])
#             serializer = CategorySerializer(obj, data=data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         elif request.method == 'PUT':
#             data = request.data
#             obj = Category.objects.get(id=data['id'])
#             serializer = CategorySerializer(obj, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         elif request.method == 'DELETE':
#             data = request.data
#             obj = Category.objects.get(id=data['id'])
#             obj.delete()
#             return Response({'message': 'Category deleted'})
#     except Category.DoesNotExist:
#         return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# consumer api
@api_view(['POST','GET','PUT','PATCH','DELETE'])
def consumer(request):
    try:
        if request.method == 'POST':
            data = request.data
            serializer = ConsumerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            objs = Consumer.objects.all()
            serializer = ConsumerSerializer(objs, many=True)
            return Response(serializer.data)

        elif request.method == 'PATCH':
            data = request.data
            obj = Consumer.objects.get(id=data['id'])
            serializer = ConsumerSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':
            data = request.data
            obj = Consumer.objects.get(id=data['id'])
            serializer = ConsumerSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            data = request.data
            obj = Consumer.objects.get(id=data['id'])
            obj.delete()
            return Response({'message': 'Consumer deleted'})
    except Consumer.DoesNotExist:
        return Response({'error': 'Consumer not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# # sub category api
# @api_view(['POST','GET','PUT','PATCH','DELETE'])
# def subcategory(request):
#     try:
#         if request.method == 'POST':
#             data = request.data
#             serializer = SubCategorySerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         elif request.method == 'GET':
#             objs = SubCategory.objects.all()
#             serializer = SubCategorySerializer(objs, many=True)
#             return Response(serializer.data)

#         elif request.method == 'PATCH':
#             data = request.data
#             obj = SubCategory.objects.get(id=data['id'])
#             serializer = SubCategorySerializer(obj, data=data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         elif request.method == 'PUT':
#             data = request.data
#             obj = SubCategory.objects.get(id=data['id'])
#             serializer = SubCategorySerializer(obj, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         elif request.method == 'DELETE':
#             data = request.data
#             obj = SubCategory.objects.get(id=data['id'])
#             obj.delete()
#             return Response({'message': 'SubCategory deleted'})
#     except SubCategory.DoesNotExist:
#         return Response({'error': 'SubCategory not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# product api
@api_view(['POST','GET','PUT','PATCH','DELETE'])
def product(request):
    try:
        if request.method == 'POST':
            data = request.data
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            objs = Product.objects.all()
            serializer = ProductSerializer(objs, many=True)
            return Response(serializer.data)

        elif request.method == 'PATCH':
            data = request.data
            obj = Product.objects.get(id=data['id'])
            serializer = ProductSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':
            data = request.data
            obj = Product.objects.get(id=data['id'])
            serializer = ProductSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            data = request.data
            obj = Product.objects.get(id=data['id'])
            obj.delete()
            return Response({'message': 'Product deleted'})
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# orders api
@api_view(['POST','GET','PUT','PATCH','DELETE'])
def order(request):
    try:
        if request.method == 'POST':
            data = request.data
            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            objs = Order.objects.all()
            serializer = OrderSerializer(objs, many=True)
            return Response(serializer.data)

        elif request.method == 'PATCH':
            data = request.data
            obj = Order.objects.get(id=data['id'])
            serializer = OrderSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':
            data = request.data
            obj = Order.objects.get(id=data['id'])
            serializer = OrderSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            data = request.data
            obj = Order.objects.get(id=data['id'])
            obj.delete()
            return Response({'message': 'Order deleted'})
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# addtocart api
@api_view(['POST','GET'])
def addtocart(request):
    try:
        if request.method == 'POST':
            data = request.data
            serializer = AddToCartSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            objs = AddToCart.objects.all()
            serializer = AddToCartSerializer(objs, many=True)
            return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# wishlist api
@api_view(['POST','GET'])
def wishList(request):
    try:
        if request.method == 'POST':
            data = request.data
            serializer = WishListSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            objs = WishList.objects.all()
            serializer = WishListSerializer(objs, many=True)
            return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['POST', 'GET', 'PUT', 'PATCH', 'DELETE'])
def review(request):
    if request.method == 'POST':
        data = request.data
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = request.data
        try:
            review = Review.objects.get(id=data['id'])
        except Review.DoesNotExist:
            return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        data = request.data
        try:
            review = Review.objects.get(id=data['id'])
        except Review.DoesNotExist:
            return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data = request.data
        try:
            review = Review.objects.get(id=data['id'])
        except Review.DoesNotExist:
            return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response({'message': 'Review deleted'}, status=status.HTTP_204_NO_CONTENT)

