from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class ProfileCreate(View):

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
