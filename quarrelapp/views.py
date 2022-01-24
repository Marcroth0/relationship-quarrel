from django.shortcuts import render
from django.http import HttpResponse
from models import Post


def detail(request, slug):
    q = Post.objects.filter(slug__iexact=slug)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    context = {

        'post': q
    }
    return render(request, 'posts/details.html', context)
