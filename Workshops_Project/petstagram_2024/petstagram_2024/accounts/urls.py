from django.urls import path,include
from petstagram_2024.accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details, name='profile-details'),
        path('edit/', views.profile_edit, name='profile-edit'),
        path ('delete/', views.delete_page, name='profile-delete'),
    ])),

]