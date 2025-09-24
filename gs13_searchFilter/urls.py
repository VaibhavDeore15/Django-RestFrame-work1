from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('demo',stdmodelviewset,basename='home')




urlpatterns = [
    path('',include(router.urls)),
    path('std/',include('rest_framework.urls')),
]
