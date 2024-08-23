from django.urls import path
from .views import item_list_create, attribute_list_create, category_list_create, item_detail

urlpatterns = [
    path('items/', item_list_create, name='item-list-create'),
    path('categories/', category_list_create, name='category-list-create'),
    path('attributes/', attribute_list_create, name='attribute-list-create'),
    path('items/<int:pk>/', item_detail, name='item-detail')
]
