from urls_views_demo.departments import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index, name='home'),
    path('redirect-to-view/', views.redirect_to_view, name='redirect-view'),
    path('softuni/', views.redirect_to_softuni),
    path('<int:pk>/', views.view_with_int_pk),
    path('<int:pk>/<slug:slug>/', views.view_with_slug, name ="pk slug"),
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.show_archive),
    path('<variable>/', views.view_with_name),
    path('<path:variable>/', views.view_with_name),
]