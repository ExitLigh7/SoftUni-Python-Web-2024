from django.urls import path
from Tasty_Recipes.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]