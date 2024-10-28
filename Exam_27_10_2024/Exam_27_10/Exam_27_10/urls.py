from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Exam_27_10.common.urls")),
    path('posts/', include("Exam_27_10.posts.urls")),
    path('authors/', include("Exam_27_10.authors.urls")),
]
