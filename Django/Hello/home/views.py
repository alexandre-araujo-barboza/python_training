from django.shortcuts import render

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

