from django.urls import path
from . import views

urlpatterns = [
    path('add_category', views.add_category,name='add_category'),
    path('edit/<int:id>', views.edit_category,name='edit_category'),
    path('delete/<int:id>', views.delete_category,name='delete_category'),
]