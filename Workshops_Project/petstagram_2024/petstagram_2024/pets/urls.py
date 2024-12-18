from django.urls import path,include
from petstagram_2024.pets.views import AddPetView, PetDetailsView, EditPetView, DeletePetView

urlpatterns = [
    path('add/', AddPetView.as_view(), name='pet-add-page'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', PetDetailsView.as_view(), name='pet-details-page'),
        path('edit/', EditPetView.as_view(), name='pet-edit-page'),
        path('delete/', DeletePetView.as_view(), name='pet-delete-page'),
    ])),
]