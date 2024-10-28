from django.urls import path
from Exam_27_10.authors import views

urlpatterns = [
    path('create/', views.AuthorCreatePage.as_view(), name='author_create'),
    path('details/', views.AuthorDetailsPage.as_view(), name='author_details'),
    path('edit/', views.AuthorEditPage.as_view(), name='author_edit'),
    path('delete/', views.AuthorDeletePage.as_view(), name='author_delete'),
]
