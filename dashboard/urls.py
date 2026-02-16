from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    # NOtes
    path('notes/', login_required(views.notes, login_url='LoginPage'), name='notes'),
    path('delete-note/<int:pk>/', login_required(views.delete_note, login_url='LoginPage'), name='delete-note'),
    path('notes-detail/<int:pk>/', login_required(views.NotesDetail, login_url='LoginPage'), name='notes-detail'),
    # Homework
    path('homework/', login_required(views.homework, login_url='LoginPage'), name='homework'),
    path('update-homework/<int:pk>/', login_required(views.update_homework, login_url='LoginPage'), name='update-homework'),
    path('delete-homework/<int:pk>/', login_required(views.delete_homework, login_url='LoginPage'), name='delete-homework'),
    # youtube
    path('youtube/', views.youtube, name='youtube'),
    # todo
    path('todo/', login_required(views.todo, login_url='LoginPage'), name='todo'),
    path('update-todo/<int:pk>/', login_required(views.update_todo, login_url='LoginPage'), name='update-todo'),
    path('delete-todo/<int:pk>/', login_required(views.delete_todo, login_url='LoginPage'), name='delete-todo'),
    
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