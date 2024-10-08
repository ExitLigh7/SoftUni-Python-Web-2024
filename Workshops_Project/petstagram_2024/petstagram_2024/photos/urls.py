from django.urls import path, include
from petstagram_2024.photos import views

urlpatterns = [
    path('add/', views.photo_add_page, name='photo-add'),
    path('<int:pk>/ ', include([
        path('',views.photo_details_page, name='photo-details-page' ),
        path('edit/',views.photo_edit_page, name='photo-edit-page'),
        path('delete/', views.photo_delete, name='photo-delete'),
    ])),
]