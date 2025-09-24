from rest_framework import serializers

class stdserializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=20)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=10)