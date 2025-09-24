from django.shortcuts import render
from rest_framework.generics import (GenericAPIView,ListAPIView,CreateAPIView,
                                     UpdateAPIView,DestroyAPIView,ListCreateAPIView,
                                     RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView)
from .models import *
from .serializer import *

# Create your views here.
# GET all + POST new
class StudentListCreate(ListCreateAPIView):
    queryset = std.objects.all()
    serializer_class = studentserializer

# GET single + PUT/PATCH + DELETE
class StudentDetail(RetrieveUpdateDestroyAPIView):
    queryset = std.objects.all()
    serializer_class = studentserializer