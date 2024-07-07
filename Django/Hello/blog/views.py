from django.shortcuts import render
from blog.data import posts

def index(request):
    context = {
        'text' : 'Say hello page at blog!',
        'title' : 'BLOG',
        'posts': posts
    }
    return render(
        request,
        'blog/index.html',
        context
    )

def post(request, id):
    
    context = {
        'text': f'Say hello to post: {id}',
        'title' : f'POST:{id}',
    }

    return render(
        request,
        'blog/example.html',
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


