from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Request
from .serializer import *
from django.core.exceptions import ObjectDoesNotExist

@api_view(['POST', 'GET', 'DELETE', 'PATCH'])
def requests(request):
    try:
        if request.method == "POST":
            data = request.data
            serializer = RequestSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            objs = Request.objects.all()
            serializer = RequestSerializer(objs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            data = request.data
            if 'id' not in data:
                return Response({'error': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                obj = Request.objects.get(id=data['id'])
                obj.delete()
                return Response({'message': 'Request deleted'}, status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({'error': 'Request not found'}, status=status.HTTP_404_NOT_FOUND)

        elif request.method == "PATCH":
            data = request.data
            if 'id' not in data:
                return Response({'error': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                obj = Request.objects.get(id=data['id'])
                serializer = RequestSerializer(obj, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                return Response({'error': 'Request not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# category api
@api_view(['POST','GET','PUT','PATCH','DELETE'])
def category(request):
    try:
        if request.method == 'POST':
            data = request.data
            serializer = CategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            objs = Category.objects.all()
            serializer = CategorySerializer(objs, many=True)
            return Response(serializer.data)

        elif request.method == 'PATCH':
            data = request.data
            obj = Category.objects.get(id=data['id'])
            serializer = CategorySerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':
            data = request.data
            obj = Category.objects.get(id=data['id'])
            serializer = CategorySerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            data = request.data
            obj = Category.objects.get(id=data['id'])
            obj.delete()
            return Response({'message': 'Category deleted'})
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# sub category api
@api_view(['POST','GET','PUT','PATCH','DELETE'])
def subcategory(request):
    try:
        if request.method == 'POST':
            data = request.data
            serializer = SubCategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            objs = SubCategory.objects.all()
            serializer = SubCategorySerializer(objs, many=True)
            return Response(serializer.data)

        elif request.method == 'PATCH':
            data = request.data
            obj = SubCategory.objects.get(id=data['id'])
            serializer = SubCategorySerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':
            data = request.data
            obj = SubCategory.objects.get(id=data['id'])
            serializer = SubCategorySerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            data = request.data
            obj = SubCategory.objects.get(id=data['id'])
            obj.delete()
            return Response({'message': 'SubCategory deleted'})
    except SubCategory.DoesNotExist:
        return Response({'error': 'SubCategory not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET', 'DELETE', 'PATCH'])
def consumerpanel(request):
    if request.method == 'GET':
        objs = ConsumerPanel.objects.all()
        serializer = ConsumerPanelSerializer(objs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        data = request.data
        try:
            obj = ConsumerPanel.objects.get(id=data['id'])
        except ObjectDoesNotExist:
            return Response({'error': 'ConsumerPanel not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ConsumerPanelSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        data = request.data
        try:
            obj = ConsumerPanel.objects.get(id=data['id'])
        except ObjectDoesNotExist:
            return Response({'error': 'ConsumerPanel not found'}, status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        return Response({'message': 'ConsumerPanel deleted'}, status=status.HTTP_204_NO_CONTENT)