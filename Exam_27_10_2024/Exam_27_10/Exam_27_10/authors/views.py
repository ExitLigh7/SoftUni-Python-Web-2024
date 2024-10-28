from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from Exam_27_10.authors.forms import AuthorCreateForm, AuthorEditForm
from Exam_27_10.authors.models import Author
from Exam_27_10.utils import get_user_obj


class AuthorCreatePage(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard')

class AuthorDetailsPage(DetailView):
    template_name = 'authors/details-author.html'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()

        last_updated_post = author.post_set.order_by('-updated_at').first()
        context['last_updated_post'] = last_updated_post
        return context

class AuthorEditPage(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('author_details')

    def get_object(self, queryset=None):
        return get_user_obj()

class AuthorDeletePage(DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()