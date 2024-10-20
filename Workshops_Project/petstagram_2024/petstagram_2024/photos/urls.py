from django.urls import path, include
from petstagram_2024.photos import views
from petstagram_2024.photos.views import PhotoAddView, PhotoEditView, PhotoDetailsView

urlpatterns = [
    path('add/', PhotoAddView.as_view(), name='photo-add'),
    path('<int:pk>/ ', include([
        path('',PhotoDetailsView.as_view(), name='photo-details-page' ),
        path('edit/',PhotoEditView.as_view(), name='photo-edit-page'),
        path('delete/', views.photo_delete, name='photo-delete'),
    ])),
]