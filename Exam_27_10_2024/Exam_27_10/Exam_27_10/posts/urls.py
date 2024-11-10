from django.urls import path,include
from Exam_27_10.posts import views

urlpatterns = [
    path('create/', views.PostCreatePage.as_view(), name='post_create'),
    path('<int:post_id>/', include([
        path('details/', views.PostDetailsPage.as_view(), name='post_details'),
        path('edit/', views.PostEditPage.as_view(), name='post_edit'),
        path('delete/', views.PostDeletePage.as_view(), name='post_delete'),
    ]))
]