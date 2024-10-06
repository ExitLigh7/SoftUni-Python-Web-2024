from django import forms
from django.core.exceptions import ValidationError
from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        error_messages = {
            'title': {
                'required': 'Please enter a title for your post.',
                'max_length': f'The title is too long! Please keep it under {Post.TITLE_MAX_LENGTH} characters.',
            },
            'author': {
                'required': 'Please enter an author name for your post.',
            }
        }

    # This validation is just for example, it would be better to be in the model
    def clean_author(self):
        author = self.cleaned_data.get('author')

        if not author[0].isupper():
            raise ValidationError("Author name must be uppercase!")

        return author

    # This type of validation is usually used for applying business logic.
    # This example is not fully suitable with the app, but it helps me understand how it works.

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title and content and title in content:
            raise ValidationError("The post title cannot be included in the post content!")

        return cleaned_data


class PostCreateForm(PostBaseForm):
    pass

class PostEditForm(PostBaseForm):
    pass

class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    disabled_fields = ("__all__",)

class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...'
            }
        ),
    )


# Without knowledge of Model Forms!

# class PostForm(forms.ModelForm):
#     title = forms.CharField(
#         max_length=100,
#     )
#     content = forms.CharField(
#         widget=forms.Textarea
#     )
#
#     author = forms.CharField(
#         max_length=30,
#     )
#
#     created_at = forms.DateTimeField()
#
#     languages = forms.ChoiceField(
#         choices=LanguageChoice.choices,
#     )