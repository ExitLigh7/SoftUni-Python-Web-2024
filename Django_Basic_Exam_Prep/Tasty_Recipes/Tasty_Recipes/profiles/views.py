from django.urls import reverse_lazy
from django.views.generic import CreateView
from Tasty_Recipes.profiles.forms import ProfileCreateForm
from Tasty_Recipes.profiles.models import Profile


class ProfileCreatePage(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('catalogue')

