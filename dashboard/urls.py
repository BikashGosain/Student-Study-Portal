from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    # NOtes
    path('notes/', views.notes, name='notes'),
    path('delete-note/<int:pk>/', views.delete_note, name='delete-note'),
    path('notes-detail/<int:pk>/', views.NotesDetail, name='notes-detail'),
    # Homework
    path('homework/', views.homework, name='homework'),
    path('update-homework/<int:pk>/', views.update_homework, name='update-homework'),
    path('delete-homework/<int:pk>/', views.delete_homework, name='delete-homework'),
    # youtube
    path('youtube/', views.youtube, name='youtube'),
    # todo
    path('todo/', views.todo, name='todo'),
    path('update-todo/<int:pk>/', views.update_todo, name='update-todo'),
    path('delete-todo/<int:pk>/', views.delete_todo, name='delete-todo'),
    
    #books
    path('books/', views.books, name='books'),
    # dictionary
    path('dictionary/', views.dictionary, name='dictionary'),
    # wiki
    path('wiki/', views.wiki, name='wiki'),
    # conversion
    path('conversion/', views.conversion, name='conversion'),
    # profile
     path('profile/', views.profile, name='profile'),
]