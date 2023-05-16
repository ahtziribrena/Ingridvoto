"""
URL configuration for votoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from crudvotaciones import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.layouts, name="layout"),
    path('', views.registrarciudadanos, name="registrarciudadanos"),
    path('enlistarciudadanos/', views.enlistarciudadanos, name="enlistarciudadanos"),
    path('eliminarciudadanos/<int:id>/', views.eliminarciudadano, name="eliminarciudadano"),
    path('editarciudadanos/<int:id>', views.editarciudadanos, name="editarciudadanos"),
    path('registrarcandidaturas/', views.registrarcandidaturas, name="registrarcandidaturas"),
    path('enlistarcandidaturas/', views.enlistarcandidaturas, name="enlistarcandidaturas"),
    path('eliminarcandidaturas/<int:id>/', views.eliminarcandidatura, name="eliminarcandidaturas"),
    path('editarcandidaturas/<int:id>', views.editarcandidaturas, name="editarcandidaturas"),
    path('registrarvotaciones/', views.registrarvotaciones, name="registrarvotaciones"),
    path('enlistarvotos/', views.enlistarvotos, name="enlistarvotos"),
]
