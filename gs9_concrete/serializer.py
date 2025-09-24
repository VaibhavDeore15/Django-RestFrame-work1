from rest_framework import serializers
from .models import *
from rest_framework.response import Response

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=std
        fields='__all__'
        
    # def validate_roll(self,value):
    #     if value>200:
    #         raise serializers.ValidationError('seat full')
    #     return value