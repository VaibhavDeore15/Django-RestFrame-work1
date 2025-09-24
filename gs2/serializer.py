from rest_framework import serializers
from .models import *

class studentserializer(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=10)
    
    def create(self, validated_data):
        return students.objects.create(**validated_data)