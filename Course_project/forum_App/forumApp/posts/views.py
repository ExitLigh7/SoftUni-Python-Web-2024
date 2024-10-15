from lib2to3.fixes.fix_input import context

from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, FormView, DetailView
from forumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet
from forumApp.posts.models import Post

class IndexView(TemplateView):

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ["common/index_logged_in.html"]
        else:
            return ["common/index.html"]


class DashboardView(ListView, FormView):
    model = Post
    template_name = "posts/dashboard.html"
    context_object_name = "posts"
    form_class = SearchForm
    paginate_by = 3
    success_url = reverse_lazy("dashboard")

    def get_queryset(self):
        queryset = self.model.objects.all()

        if "query" in self.request.GET:
            query = self.request.GET.get("query")
            queryset = self.queryset.filter(title__icontains=query)
        return queryset


class AddPostView(CreateView):
    model = Post
    fields = "__all__"
    template_name = "posts/add_post.html"
    success_url = reverse_lazy("dashboard")


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

class DetailPostView(DetailView):
    model = Post
    template_name = "posts/details-post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formset"] = CommentFormSet()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        formset = CommentFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

        context = self.get_context_data()
        context["formset"] = formset

        return self.render_to_response(context)


class DeletePostView(DeleteView,FormView):
    model = Post
    form_class = PostDeleteForm
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy("dashboard")

    def get_initial(self):
        pk = self.kwargs.get("pk")
        post = Post.objects.get(pk=pk)
        return post.__dict__








