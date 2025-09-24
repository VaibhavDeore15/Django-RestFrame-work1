from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .serializer import *
import io
import json
from rest_framework.renderers import JSONRenderer
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)  # ✅ Read from query params
        if id is not None:
            stu = student.objects.get(id=id)
            serializer = studentserializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = student.objects.all()
        serializer = studentserializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=studentserializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'DATA created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
        
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=student.objects.get(id=id)
        serializer=studentserializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'DATA Updated!!!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
     
     # delete data
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=student.objects.get(id=id)
        stu.delete()
        res={'msg':'DATA DELETED!!!'}
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=False)