from django.urls import path
from petstagram_2024.common import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
]