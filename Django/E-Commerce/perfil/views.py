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
        self.perfil = None

        if self.request.user.is_authenticated:
            self.perfil = models.Perfil.objects.filter(
                usuario = self.request.user
            ).first

            self.contexto = {
                'userform': forms.UserForm(
                    data = self.request.POST or None,
                    username = self.request.user,
                    instance = self.request.user,
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
        
        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']  
        self.renderizar = render(self.request, self.template_name, self.contexto)

    def get(self, *args, **kargs):
        return self.renderizar

class ProfileCreate(BaseProfile):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid():
            return self.renderizar
        
        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        if self.request.user.is_authenticated:
            pass
        else:
            username = self.userform.save(commit = False)

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
