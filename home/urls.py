from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.home, name='home'),
    
    path('projects/', views.projects, name='projects'),

    path('contact/', views.contact, name='contact'),
    
    path('weather/', views.runner, name='weather'),

]