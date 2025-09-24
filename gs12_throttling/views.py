from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .models import *
from .serializer import *
from rest_framework.permissions import (AllowAny,IsAdminUser,
                                        IsAuthenticated,IsAuthenticatedOrReadOnly)
from rest_framework.authentication import (BasicAuthentication,SessionAuthentication,
                                        )
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

# Create your views here.
class stdmodelviewset(ModelViewSet):
    queryset=std.objects.all()
    serializer_class=studentserializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    #throttling-->
    throttle_classes=[AnonRateThrottle,UserRateThrottle]
    
    """Here i have created token for user to perform crud oprations
        for that steps:-
        1) add this --> 'rest_framework.authtoken' at settings.py in installed_apps[]
        2) use command --> python manage.py drf_create_token admin
        3) you can see token --> Generated token 'cb30ef447b2165e9342e3a8c7e605d72b6dfd138' for user admin
        4) In postman choose bariar token and Enter Token
        5) Hit the requests as you set

        """
