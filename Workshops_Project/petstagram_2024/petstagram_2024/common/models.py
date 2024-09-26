from django.db import models

from petstagram_2024.photos.models import Photo


class PhotoComment(models.Model):
    text = models.TextField(
        max_length=300,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )

class PhotoLike(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )
