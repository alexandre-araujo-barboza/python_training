from blog import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('example/', views.example),
]