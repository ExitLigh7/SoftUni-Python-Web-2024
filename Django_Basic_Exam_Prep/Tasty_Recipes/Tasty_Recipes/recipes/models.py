from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

class Recipe(models.Model):
    CUISINE_CHOICES = [
        ('FR', 'French'),
        ('CH', 'Chinese'),
        ('IT', 'Italian'),
        ('BA', 'Balkan'),
        ('OT', 'Other'),
    ]

    title = models.CharField(
        unique=True,
        max_length=100,
        validators=[
            MinLengthValidator(10)
        ],
        error_messages={
            'unique': "We already have a recipe with the same title!"
        }
    )

    cuisine_type = models.CharField(
        max_length=7,
        choices=CUISINE_CHOICES,
    )

    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space.",
    )

    instructions = models.TextField()

    cooking_time = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
        ],
        help_text="Provide the cooking time in minutes.",
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    author = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
    )