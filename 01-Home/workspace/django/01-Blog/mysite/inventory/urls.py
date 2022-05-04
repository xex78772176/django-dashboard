from django.urls import path
from . import views
urlpatterns = [
path('', views.index),
path('price/', views.price),
path('user/', views.user),
path('year/', views.year),
]