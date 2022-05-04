from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('W311-H3/',views.W311H3),
    path('W311a/',views.W311a),
    path('W311H1/',views.W311H1),
    path('W311D-Z2/',views.W311Z2),
    path('W311D-Z1/',views.W311DZ1),
    path('W311-H2/',views.W311H2),
    path('W311b/',views.W311b),
]