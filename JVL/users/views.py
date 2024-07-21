from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *

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
        serializer = ProfileSerializer(objs ,many = True)
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
