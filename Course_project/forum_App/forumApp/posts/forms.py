from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory
from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post, Comment


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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'Author name is required. Write it!',
            },
            'content': {
                'required': 'Content is required. Write it!',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add message...',
            'rows': 1,
        })

CommentFormSet = formset_factory(CommentForm, extra=1)