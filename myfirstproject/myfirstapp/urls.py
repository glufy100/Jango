from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('bonjour/', views.bonjour, name='bonjour'),
    path('formulaire/', views.formulaire, name='formulaire'),
]