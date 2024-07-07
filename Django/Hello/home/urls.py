from home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('example/', views.example, name='home_example'),
]
