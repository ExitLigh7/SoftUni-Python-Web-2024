from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Tasty_Recipes.common.urls')),
    path('recipe/', include('Tasty_Recipes.recipes.urls')),
    path('profile/', include('Tasty_Recipes.profiles.urls')),
]
