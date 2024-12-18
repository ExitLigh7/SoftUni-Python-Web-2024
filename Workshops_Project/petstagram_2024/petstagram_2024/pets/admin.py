from django.contrib import admin
from petstagram_2024.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
