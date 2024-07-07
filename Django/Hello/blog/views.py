from django.shortcuts import render

def index(request):
    context = {
        'text' : 'Say hello page at blog!',
        'title' : 'BLOG'
    }
    return render(
        request,
        'blog/index.html',
        context
    )

def example(request):
    context = {
        'text' : 'Say hello page at blog example!',
        'title' : 'BLOG - EXAMPLE'
    }
    return render(
        request,
        'blog/example.html',
        context
    )


