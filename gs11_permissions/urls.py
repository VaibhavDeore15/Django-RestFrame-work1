from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('per',stdmodelviewset,basename='per')




urlpatterns = [
    path('demo/',include(router.urls)),
    path('std/',include('rest_framework.urls')),
]
