from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .models import *
from rest_framework.permissions import AllowAny
from .serializer import *

# Create your views here.
class stdmodelviewset(ModelViewSet):
    queryset=std.objects.all()
    serializer_class=studentserializer
    permission_classes = [AllowAny]
    
# class stdmodelviewset(ReadOnlyModelViewSet):
#     queryset=std.objects.all()
#     serializer_class=studentserializer