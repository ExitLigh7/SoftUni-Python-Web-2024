from django.urls import path
from Exam_27_10.common import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='home'),
    path('dashboard/', views.DashboardPage.as_view(), name='dashboard'),
]