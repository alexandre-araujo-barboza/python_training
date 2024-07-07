from django.shortcuts import render

def index(request):
    context = {
        'text' : 'Say hello page at blog!'
    }
    return render(
        request,
        'blog/index.html',
        context
    )

def example(request):
    context = {
        'text' : 'Say hello page at blog example!'
    }
    return render(
        request,
        'blog/example.html',
        context
    )


