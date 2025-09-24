from django.urls import path
from .views import *

urlpatterns = [
    path('home/',StudentListCreate.as_view()),
    path('home/<int:pk>/',StudentDetail.as_view()),
]
