from rest_framework import serializers
from .models import *

class studentserializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
# Validation feild
    """def validate_roll(self,value):
        if value>200:
            raise serializers.ValidationError('Seat Full')
        return value
    def validate_city(self,value):
        if value=='US':
            raise serializers.ValidationError('US city is not acceptable')"""
            
# Object level Validation 
    def validate(self, data):
        name=data.get('name')
        city=data.get('city')
        if name.lower()=='rakesh' and city!='nsk':
            raise serializers.ValidationError('City must nsk')
        return data
    
    """if we are use normal serializer and we want to perform CURD operations we need to define functions as below,
    but if we are use modelSerializer we dont need to define this functions , model serializer provied this functions automatically """ 
# partial UPDATE
    """def update(self, instance, validated_data):
        print(instance.name)
        print(instance.roll)
        print(instance.city)
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance"""
    
# Create Data
"""    def create(self, validated_data):
        return student.objects.create(**validated_data)"""
        