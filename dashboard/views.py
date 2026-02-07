from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import *

# Create your views here.

def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, f'Note created from {request.user.username} successfully!')
            form = NotesForm()
        
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {
        'notes': notes,
        'form': form,
    }
    return render(request, 'dashboard/notes.html', context)


def delete_note(request, pk=None):
    Notes.objects.get(id=pk).delete()
    messages.success(request, f'Note deleted from {request.user.username} successfully!')
    return redirect('notes')

def NotesDetail(request, pk=None):
    note = Notes.objects.get(id=pk)
    context = {
        'note': note,
    }
    return render(request, 'dashboard/notes_detail.html', context)