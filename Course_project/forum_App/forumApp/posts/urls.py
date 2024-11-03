from django.urls import path, include
from forumApp.posts.views import IndexView, AddPostView, EditPostView, DeletePostView, DashboardView, DetailPostView, \
    approve_post

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('<int:pk>/', include([
        path('approve-post/', approve_post, name='approve_post'),
        path('delete-post/', DeletePostView.as_view(), name='delete-post'),
        path('details-post/', DetailPostView.as_view(), name='details-post'),
        path('edit-post/', EditPostView.as_view(), name='edit-post'),
    ]))
]