from django.urls import path,include
from Tasty_Recipes.recipes import views

urlpatterns = [
    path('catalogue/', views.RecipeCataloguePage.as_view(), name='catalogue'),
    path('create/', views.RecipeCreatePage.as_view(), name='recipe_create'),
    path('<int:recipe_id>/', include([
        path('details/', views.RecipeDetailsPage.as_view(), name='recipe_details'),
    ]))
]