from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from Tasty_Recipes.recipes.forms import RecipeCreateForm
from Tasty_Recipes.recipes.models import Recipe
from Tasty_Recipes.utils import get_user_obj


class RecipeCataloguePage(ListView):
    model = Recipe
    template_name = "recipes/catalogue.html"
    context_object_name = "recipes_catalogue"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_recipes'] = self.get_queryset().exists()  # Check if there are any recipes
        return context

class RecipeCreatePage(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipes/create-recipe.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)

class RecipeDetailsPage(DetailView):
    model = Recipe
    pk_url_kwarg = 'recipe_id'
    template_name = 'recipes/details-recipe.html'

    def get_context_data(self, **kwargs):
        # Get the existing context from the parent class
        context = super().get_context_data(**kwargs)

        # Access the Recipe instance (the object for this DetailView)
        recipe = self.get_object()

        # Split the ingredients field by ", "
        context['split_ingredients'] = recipe.ingredients.split(", ")

        return context