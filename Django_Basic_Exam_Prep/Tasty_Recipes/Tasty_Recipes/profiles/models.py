from django.core.validators import MinLengthValidator
from django.db import models

from Tasty_Recipes.profiles.validators import CapFirstValidator


class Profile(models.Model):
    nickname = models.CharField(
        unique=True,
        max_length=20,
        validators=[
            MinLengthValidator(2, "Nickname must be at least 2 chars long!"),
        ],
    )

    first_name = models.CharField(
        max_length=30,
        validators=[
            CapFirstValidator(),
        ]
    )

    last_name = models.CharField(
        max_length=30,
        validators=[
            CapFirstValidator(),
        ]
    )

    chef = models.BooleanField(
        default=False,
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )