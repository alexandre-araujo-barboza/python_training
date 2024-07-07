from django.shortcuts import render

def index(request):
    context = {
      'text' : 'Say hello to home page!',
      'title' : 'HOME'
    }
    return render(
        request,
        'home/index.html',
        context
    )

def example(request):
    context = {
        'text' : 'Say hello to home page of example!',
        'title' : 'HOME - EXAMPLE'
    }
    return render(
        request,
        'home/example.html',
        context
    )

