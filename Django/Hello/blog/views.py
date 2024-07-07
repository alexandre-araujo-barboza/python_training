from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello page as blog!')

def exemplo(request):
    return HttpResponse('Hello page as blog (example)!')


