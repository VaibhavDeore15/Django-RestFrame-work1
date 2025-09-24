from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homemixin.as_view()),
    path('home/<int:pk>/',homemixin.as_view()),
]
