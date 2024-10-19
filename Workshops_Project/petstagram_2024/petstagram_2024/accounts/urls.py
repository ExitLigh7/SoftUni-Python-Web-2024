from django.urls import path,include
from petstagram_2024.accounts import views
from petstagram_2024.pets.views import DeletePetView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details, name='profile-details'),
        path('edit/', views.profile_edit, name='profile-edit'),
        path ('delete/', DeletePetView.as_view(), name='profile-delete'),
    ])),

]