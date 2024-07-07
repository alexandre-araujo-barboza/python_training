from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello page as home!')

def exemplo(request):
    return HttpResponse('Hello page as home (example)!')


