from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from forumApp.posts.forms import PostBaseForm, PostCreateForm, PostDeleteForm
from forumApp.posts.models import Post


def index(request):

    context = {
        "my_form": "",
    }

    return render(request, 'base.html', context)

def dashboard(request):
    context = {
        "posts": Post.objects.all(),
    }

    return render(request, "posts/dashboard.html", context)

def add_post(request):
    form = PostCreateForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        "form": form,
    }
    return render(request, "posts/add_post.html", context)

def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == "POST":
        post.delete()
        return redirect('dashboard')

    context = {
        "form": form,
        'post': post,
    }

    return render(request, "posts/delete_post.html", context)





