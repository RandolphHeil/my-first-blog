from django.shortcuts import render, get_object_or_404


def post_list(request):
    return render(request, 'blog/post_list.html', {})

from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    return render(request, 'blog/post_list.html', {"post":post})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {"post":post})
