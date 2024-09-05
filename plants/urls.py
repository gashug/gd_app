from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    path('create/', views.plant_create, name='plant_create'),
    path('<int:pk>/', views.plant_detail, name='plant_detail'),
]
