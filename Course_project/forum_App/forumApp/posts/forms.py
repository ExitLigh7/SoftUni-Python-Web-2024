from django import forms

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