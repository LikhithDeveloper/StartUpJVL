from rest_framework import serializers
from .models import *
from users.models import*

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'