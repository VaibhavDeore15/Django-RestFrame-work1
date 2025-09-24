from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .models import *
from .serializer import *
from rest_framework.permissions import (AllowAny,IsAdminUser,
                                        IsAuthenticated,)
from rest_framework.authentication import (BasicAuthentication,SessionAuthentication,
                                        )
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import filters



# Create your views here.
class stdmodelviewset(ModelViewSet):
    queryset=std.objects.all()
    serializer_class=studentserializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[AllowAny]
    
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['roll','city']
    # search_fields=['^city']
    
    ordering_fields=['name','id']
    
