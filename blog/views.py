from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm


def post_list(request):
    return render(request, 'blog/post_list.html', {})

from django.utils import timezone
from .models import Post

def post_list(request):
    post = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    return render(request, 'blog/post_list.html', {"post":post})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {"post":post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {"form": form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
