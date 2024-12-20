from django.urls import path
from petstagram_2024.common import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('like/<int:photo_id>/', views.likes_functionality, name='like'),
    path('share/<int:photo_id>/', views.share_functionality, name='share'),
    path('comment/<int:photo_id>/', views.comments_functionality, name='comment'),
]