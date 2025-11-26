from django.urls import path
from .views import category_list, category_details

urlpatterns = [
    path('', category_list, name='category-list'),
    path('<int:pk>/', category_details, name='category-details'),
]
