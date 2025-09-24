"""
URL configuration for myapi_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gs1.urls')),
    path('gs2/',include('gs2.urls')),
    path('gs3/',include('gs3CRUD.urls')),
    path('gs4/',include('gs4_model_seri.urls')),
    path('gs5/',include('gs5_FBV.urls')),
    path('gs6/',include('gs6_FBC_CURD.urls')),
    path('gs7/',include('gs7_FBV_Browser.urls')),
    path('gs8/',include('gs8_mixin_generic.urls')),
    path('gs9/',include('gs9_concrete.urls')),
    path('gs10/',include('gs10_modelviewset.urls')),
    path('gs11/',include('gs11_permissions.urls')),
    path('gs12/',include('gs12_throttling.urls')),
    path('gs13',include('gs13_searchFilter.urls')),
]
