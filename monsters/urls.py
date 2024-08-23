from django.urls import path
from .views import monster_list_create, monster_detail

urlpatterns = [
    path('monsters/', monster_list_create, name='monster-list-create'),
    path('monsters/<int:pk>/', monster_detail, name='monster-detail'),
]