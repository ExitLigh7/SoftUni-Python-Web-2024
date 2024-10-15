from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, FormView
from forumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm
from forumApp.posts.models import Post

class IndexView(TemplateView):

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ["common/index_logged_in.html"]
        else:
            return ["common/index.html"]


# def index(request):
#
#     context = {
#         "my_form": "",
#     }
#
#     return render(request, 'common/index.html', context)

class DashboardView(ListView, FormView):
    model = Post
    template_name = "posts/dashboard.html"
    context_object_name = "posts"
    form_class = SearchForm
    success_url = reverse_lazy("dashboard")

    def get_queryset(self):
        queryset = self.model.objects.all()

        if "query" in self.request.GET:
            query = self.request.GET.get("query")
            queryset = self.queryset.filter(title__icontains=query)
        return queryset


# def dashboard(request):
#     form =  SearchForm(request.GET)
#     posts = Post.objects.all()
#
#     if request.method == "GET":
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             posts = posts.filter(title__icontains=query)
#
#     context = {
#         "posts": posts,
#         "form": form,
#     }
#
#     return render(request, "posts/dashboard.html", context)

class AddPostView(CreateView):
    model = Post
    fields = "__all__"
    template_name = "posts/add_post.html"
    success_url = reverse_lazy("dashboard")

# def add_post(request):
#     form = PostCreateForm(request.POST or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#
#     context = {
#         "form": form,
#     }
#     return render(request, "posts/add_post.html", context)

class EditPostView(UpdateView):
    model = Post
    form_class = PostEditForm
    fields = "__all__"
    template_name = "posts/edit-post.html"
    success_url = reverse_lazy("dashboard")

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields = "__all__")
        else:
            return modelform_factory(Post, fields = ("content",))

# def edit_post(request, pk:int):
#     post = Post.objects.get(pk=pk)
#
#     if request.method == "POST":
#         form = PostEditForm(request.POST, instance=post)
#
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = PostEditForm(instance=post)
#
#     context = {
#         "form": form,
#         "post": post,
#     }
#
#     return render(request, 'posts/edit-post.html', context)

def details_page(request, pk:int):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post,
    }
    return render(request, 'posts/details-post.html', context)

class DeletePostView(DeleteView,FormView):
    model = Post
    form_class = PostDeleteForm
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy("dashboard")

    def get_initial(self):
        pk = self.kwargs.get("pk")
        post = Post.objects.get(pk=pk)
        return post.__dict__


# def delete_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     form = PostDeleteForm(instance=post)
#
#     if request.method == "POST":
#         post.delete()
#         return redirect('dashboard')
#
#     context = {
#         "form": form,
#         'post': post,
#     }
#
#     return render(request, "posts/delete_post.html", context)







