from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(
        request,
        'home/index.html'
    )

def example(request):
    return render(
        request,
        'home/example.html'
    )

