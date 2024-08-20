"""
URL configuration for thotex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from rest_framework import routers
from .viewsets import *
from . import views
from .views import *

# router = routers.SimpleRouter()
# router.register('personas', PersonaViewSet)

urlpatterns = [
   path('register', RegisterView.as_view(), name='register'),
   path('login', LoginView.as_view(), name='login'),
   path('user', UserView.as_view(), name='user'),
   path('logout', LogoutView.as_view(), name='logout'),
   path('municipios/', MunicipioLista.as_view(), name='municipios'),
   path('municipios/<int:pk>', MunicipioDetalle.as_view(), name='municipio'),
   path('departamentos/', DepartamentoLista.as_view(), name='departamentos'),
   path('departamentos/<int:pk>', DepartamentoDetalle.as_view(), name='departamento'),
   path('departamento/<int:Dep_id>/municipios/', DepartamentoMunicipiosListView.as_view(), name='departamento-municipios'),
   path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activate'),
]

# urlpatterns = router.urls
