from rest_framework import serializers
from .models import *

"""Here we using model serializer we dont need to wory about CRUD operations"""
class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'