from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializer import *
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def single(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        print(pythondata)#here we get python data as dict 
        serializer=studentserializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data created'})
        json_d=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_d,content_type='application/json')