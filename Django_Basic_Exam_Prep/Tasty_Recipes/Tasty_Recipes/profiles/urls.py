from django.urls import path
from Tasty_Recipes.profiles import views

urlpatterns = [
path('create/', views.ProfileCreatePage.as_view(), name='profile_create'),
]