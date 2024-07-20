from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpRequest, HttpResponse
from . import models
from . import forms
class BaseProfile(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        if self.request.user.is_authenticated:
            self.contexto = {
                'userform': forms.UserForm(
                    data = self.request.POST or None,
                    username = self.request.user,
                    instance = self.request.user,
                    password = self.request.POST.get('password'),
                    email    = self.request.POST.get('email'),
                ),
                'perfilform' : forms.PerfilForm(
                    data = self.request.POST or None
                )
            }
        else:
            self.contexto = {
                'userform': forms.UserForm(
                    data = self.request.POST or None
                ),
                'perfilform' : forms.PerfilForm(
                    data = self.request.POST or None
                )
            }

        self.renderizar = render(self.request, self.template_name, self.contexto)

    def get(self, *args, **kargs):
        return self.renderizar

class ProfileCreate(BaseProfile):
    def post(self, *args, **kwargs):
        return self.renderizar

class ProfileUpdate(View):

    def get(self, *args, **kargs):
        return HttpResponse('atualizar')

class ProfileLogin(View):

    def get(self, *args, **kargs):
        return HttpResponse('login')

class ProfileLogout(View):

    def get(self, *args, **kargs):
        return HttpResponse('logout')
