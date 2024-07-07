from blog import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='blog'),
    path('<int:post_id>/', views.post, name='post'),
    path('example/', views.example, name='blog_example'),
]
