from django.urls import path,include
from.views import *

urlpatterns = [
    path('',single_data),
    path('all/',all_data),
]
