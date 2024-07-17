from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path(
        '',
        views.ProfileCreate.as_view(),
        name='criar'
    ),
    path(
        'atualizar/',
        views.ProfileUpdate.as_view(),
        name='atualizar'
    ),
    path(
        'login/',
        views.ProfileLogin.as_view(),
        name='login'
    ),
    path(
        'logout/',
        views.ProfileLogout.as_view(),
        name='logout'
    ),
]

