from django import forms

from Exam_27_10.mixins import ReadOnlyMixin
from Exam_27_10.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['updated_at','author',]

class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        labels = {
            "image_url": "Post Image URL:"
        }


    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'placeholder': 'Put an attractive and unique title...'})
        self.fields['content'].widget.attrs.update(
            {
                'placeholder': 'Share some interesting facts about your adorable pets...',
            }
        )

class PostEditForm(PostBaseForm,):
    class Meta(PostBaseForm.Meta):
        labels = {
            "image_url": "Post Image URL:"
        }

class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    read_only_fields = ["title", "image_url", "content"]