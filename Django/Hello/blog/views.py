from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello page as blog!')

def example(request):
    return HttpResponse('Hello page as blog (example)!')


