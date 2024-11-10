from django import forms
from Tasty_Recipes.recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author',]

class RecipeCreateForm(RecipeBaseForm):
    def __init__(self, *args, **kwargs):
        super(RecipeCreateForm, self).__init__(*args, **kwargs)

        # Adding placeholders to specific fields
        self.fields['ingredients'].widget.attrs.update({'placeholder': 'ingredient1, ingredient2, ...'})
        self.fields['instructions'].widget.attrs.update({'placeholder': 'Enter detailed instructions here...'})
        self.fields['image_url'].widget.attrs.update({'placeholder': 'Optional image URL here...'})

class RecipeEditForm(RecipeBaseForm):
    pass

class RecipeDeleteForm(RecipeBaseForm):
    pass