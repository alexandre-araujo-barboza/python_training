from blog import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('exemplo/', views.exemplo),
]