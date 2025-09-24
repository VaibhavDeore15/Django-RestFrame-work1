from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .models import *
from .serializer import *
from rest_framework.permissions import (AllowAny,IsAdminUser,
                                        IsAuthenticated,)
from rest_framework.authentication import (BasicAuthentication,SessionAuthentication,
                                        )
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# user=User.objects.get(username='harsh')
# tk=Token.objects.create(user=user)
# print(tk) 

# Create your views here.
class stdmodelviewset(ModelViewSet):
    queryset=std.objects.all()
    serializer_class=studentserializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]
