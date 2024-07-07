from blog import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='blog'),
    path('example/', views.example, name='blog_example'),
    path('post/<int:id>', views.post, name='post'),
]
