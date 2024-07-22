from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Request
from .serializer import RequestSerializer
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
