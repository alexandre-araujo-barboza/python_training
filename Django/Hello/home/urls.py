from home import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('example/', views.exemplo),
]