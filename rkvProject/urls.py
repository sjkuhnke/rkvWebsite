"""
URL configuration for rkvProject project.

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
from django.urls import path
from rkvApp import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('documentary/', views.documentary, name='documentary'),
    path('show/', views.show, name='show'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]

handler404 = 'rkvApp.views.custom_404'
