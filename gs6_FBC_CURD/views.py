from django.shortcuts import render,HttpResponse
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *

# Create your views here.
@api_view(['GET','PUT','POST','DELETE'])
def home(request):
    if request.method=='GET':
        id=request.query_params.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=studentserializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=studentserializer(stu,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'save'})

        return Response(serializer.errors)
    
    if request.method=='PUT':
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        serializer=studentserializer(stu,data=request.data,
                                     partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    if request.method=='DELETE':
        id=request.data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            stu.delete()
            # return Response({'data':'Deleted'})
            return HttpResponse('hjbdjbwj')