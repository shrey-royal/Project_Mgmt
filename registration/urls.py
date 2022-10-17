from django.urls import path
from . import views

urlpatterns = [
    path('insert-role/', views.insert_role, name='insert-role'),
    path('show-role/', views.show_roles, name='show-roles'),
    path('edit-role/<int:id>/', views.edit_role, name='edit-role'),
    path('delete-role/<int:id>/', views.delete_role, name='delete-role'),
]