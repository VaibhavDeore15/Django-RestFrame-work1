from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

#model object single data
def single_data(request):
    stu=std.objects.get(id=2)
    ser=stdserializer(stu)
    # json_data=JSONRenderer().render(ser.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(ser.data)

#Query set (all Data)
def all_data(request):
    stu=std.objects.all()
    ser=stdserializer(stu,many=True)
    # json_data=JSONRenderer().render(ser.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(ser.data,safe=False)
