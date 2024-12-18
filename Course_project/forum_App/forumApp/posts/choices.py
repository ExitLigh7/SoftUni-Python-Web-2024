from django.db import models


class LanguageChoice(models.TextChoices):
    # the first value is what is stored in the DB and the second one is what we show on the user
    PYTHON = "py", "Python"
    JAVASCRIPT = "jS", "JavaScript"
    C = "c", "C"
    C_PLUS_PLUS = "cpp", "C++"
    OTHER = "other", "Other"
