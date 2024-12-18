from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.apps import apps


# # The better way is to do it with class because we can redefine the bad words as argument

# def bad_language_validator(value):
#     bad_words = ['bad_word1', 'bad_word2', 'bad_word3']
#
#     for bad_word in bad_words:
#         if bad_word.lower() in value.lower():
#             raise ValidationError("The text contains bad language!")


@deconstructible
class BadLanguageValidator:

    def __init__(self, bad_words=None):
        if bad_words is None:
            self.bad_words = ['bad_word1', 'bad_word2', 'bad_word3']
        else:
            self.bad_words = bad_words

    def __call__(self, value):
        for bad_word in self.bad_words:
            if bad_word.lower() in value.lower():
                raise ValidationError("The text contains bad language!")


@deconstructible
class UniquePostTitleValidator:

    def __init__(self, exclude_post=None):

        self.exclude_post = exclude_post

    def __call__(self, value):
        post = apps.get_model('posts', 'Post')
        normalized_value = value.strip().lower()
        queryset = post.objects.filter(title__iexact=normalized_value)

        if self.exclude_post:
            queryset = queryset.exclude(pk=self.exclude_post.pk)

        if queryset.exists():
            raise ValidationError("Warning, this title already exists!")

    def __eq__(self, other):
        return (
                isinstance(other, UniquePostTitleValidator) and
                self.exclude_post == other.exclude_post
        )

