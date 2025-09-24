from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework import status

# Create your views here.
@api_view(['GET','PUT','PATCH','POST','DELETE'])
def home(request,id=None):
    if request.method=='GET':
        if id is not None:
            stu=std.objects.get(id=id)
            serializer=studentserializer(stu)
            return Response(serializer.data)
        stu=std.objects.all()
        serializer=studentserializer(stu,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='PUT':
        stu=std.objects.get(pk=id)
        serializer=studentserializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)
    
    if request.method=='PATCH':
        stu=std.objects.get(pk=id)
        serializer=studentserializer(stu,data=request.data,
                                     partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)
    
    
    if request.method=='DELETE':
        if id is not None:
            stu=std.objects.get(id=id)
            stu.delete()
            return Response({'data':'Deleted'})
        return Response({'msg':'Enter valid id'})