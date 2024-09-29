from django import forms
from forumApp.posts.choices import LanguageChoice
from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


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