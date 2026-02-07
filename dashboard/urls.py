from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('notes/', views.notes, name='notes'),
    path('delete-note/<int:pk>/', views.delete_note, name='delete-note'),
    path('notes-detail/<int:pk>/', views.NotesDetail, name='notes-detail'),
]