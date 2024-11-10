from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from Exam_27_10.posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from Exam_27_10.posts.models import Post
from Exam_27_10.utils import get_user_obj


class PostCreatePage(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)

class PostDetailsPage(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/details-post.html'

class PostEditPage(UpdateView):
    model = Post
    form_class = PostEditForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dashboard')

class PostDeletePage(DeleteView):
    model = Post
    form_class = PostDeleteForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
