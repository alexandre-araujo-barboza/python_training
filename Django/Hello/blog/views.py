from django.shortcuts import render
from django.http import HttpRequest, Http404
from blog.data import posts
from typing import Any

def index(request):
    context = {
        'text' : 'Say hello to blog page!',
        'title' : 'BLOG',
        'posts': posts
    }
    return render(
        request,
        'blog/index.html',
        context
    )

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404(f'This post ({post_id}) does not exist.')

    context = {
        'text': f'Say hello to post: {post_id}!',
        'title' : f'POST: {post_id}',
        'post' : found_post,
    }

    return render(
        request,
        'blog/post.html',
        context
    )
    
def example(request):
    context = {
        'text' : 'Say hello to blog page of example!',
        'title' : 'BLOG - EXAMPLE'
    }
    return render(
        request,
        'blog/example.html',
        context
    )


