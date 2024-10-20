from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from petstagram_2024.common.forms import CommentForm
from petstagram_2024.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram_2024.photos.models import Photo

class PhotoAddView(CreateView):
    model = Photo
    form_class = PhotoAddForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home-page')

class PhotoEditView(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('photo-details-page', kwargs={'pk': self.object.pk})


def photo_delete(request, pk: int):
    Photo.objects.get(pk=pk).delete()
    return redirect('home-page')


class PhotoDetailsView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['likes'] = self.object.like_set.all()
        context['comments'] = self.object.comment_set.all()
        return context
