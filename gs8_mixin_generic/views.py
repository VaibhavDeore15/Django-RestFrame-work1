from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin,ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import *
from .serializer import *

# Create your views here.
class homemixin(GenericAPIView,CreateModelMixin,ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset =std.objects.all()
    serializer_class=studentserializer
    
    def get(self,request,pk=None):
        if pk:
            return self.retrieve(request,pk=pk)
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    def put(self,request,pk):
        return self.update(request,pk=pk)
    
    def patch(self,request,pk):
        return self.partial_update(request,pk=pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk=pk)