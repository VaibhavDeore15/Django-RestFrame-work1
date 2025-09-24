from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('home/<int:id>',home),
]
