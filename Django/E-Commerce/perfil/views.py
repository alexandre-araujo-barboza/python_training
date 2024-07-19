from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpRequest, HttpResponse
from . import models
from . import forms
class BaseProfile(View):
    template_name = 'perfil/criar.html'

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        super().setup(request, *args, **kwargs)
        self.contexto = {
            'userform': forms.UserForm(
                data = self.request.POST or None
            ),
            'perfilform' : forms.PerfilForm(
                data = self.request.POST or None
            ),
        },
        self.renderizar = render(self.request, self.template_name, self.contexto)

    def get(self, *args, **kargs):
        return self.renderizar

class ProfileCreate(BaseProfile):

    def get(self, *args, **kargs):
        return HttpResponse('criar')

class ProfileUpdate(View):

    def get(self, *args, **kargs):
        return HttpResponse('atualizar')

class ProfileLogin(View):

    def get(self, *args, **kargs):
        return HttpResponse('login')

class ProfileLogout(View):

    def get(self, *args, **kargs):
        return HttpResponse('logout')
