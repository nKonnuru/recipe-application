from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('new/', views.recipe_create, name='recipe_create'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('<int:pk>/edit/', views.recipe_update, name='recipe_update'),
    path('<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
    path('simple_report/', views.recipe_report, name='recipe_report'),
    path('advanced-report/', views.advanced_report, name='advanced_report'),
]
