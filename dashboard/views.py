from urllib import request
import requests
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
import scrapetube
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
            return redirect('notes')
        
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

def homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            homework = form.save(commit=False)
            homework.user = request.user
            homework.save()
            messages.success(request, 'Homework added successfully!')
            return redirect('homework')
    else:
        form = HomeworkForm()

    homework = Homework.objects.filter(user=request.user)

    homework_done = not homework.filter(is_finished=False).exists()

    context = {
        'homework': homework,
        'homework_done': homework_done,
        'form': form,
    }
    return render(request, 'dashboard/homework.html', context)

def update_homework(request, pk=None):
    homework = get_object_or_404(Homework, id=pk, user=request.user)
    homework.is_finished = not homework.is_finished
    homework.save()
    next_page = request.GET.get('next', 'homework')
    return redirect(next_page)


def delete_homework(request, pk):
    hw = get_object_or_404(Homework, id=pk, user=request.user)
    hw.delete()
    messages.success(request, f'Homework "{hw.title}" deleted successfully!')
    next_page = request.GET.get('next', 'profile')
    return redirect(next_page)


def youtube(request):
    results = []

    if request.method == 'POST':
        form = YoutubeForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            videos = scrapetube.get_search(query, limit=10)

            for video in videos:
                # Title
                title = ''
                if 'title' in video and 'runs' in video['title']:
                    title = ''.join([r.get('text', '') for r in video['title']['runs']])

                # Description
                description = ''
                if 'descriptionSnippet' in video:
                    description = ''.join([r.get('text', '') for r in video['descriptionSnippet']])

                # Channel
                channel = video.get('author', {}).get('title', 'Unknown channel')

                # Duration
                duration = video.get('lengthSeconds', None)
                if duration:
                    minutes = int(duration) // 60
                    seconds = int(duration) % 60
                    duration = f"{minutes}:{seconds:02d}"
                else:
                    duration = 'Unknown sec'

                # Published
                published = ''
                if 'publishedTimeText' in video:
                    published = video['publishedTimeText'].get('simpleText', '')

                # Thumbnail
                thumbnail = ''
                thumbs = video.get('thumbnails', [])
                if thumbs:
                    thumbnail = thumbs[-1].get('url', '')
                    if thumbnail.startswith('//'):
                        thumbnail = 'https:' + thumbnail

                # Link
                video_id = video.get('videoId', '')
                link = f"https://www.youtube.com/watch?v={video_id}" if video_id else '#'

                results.append({
                    'title': title,
                    'description': description,
                    'channel': channel,
                    'duration': duration,
                    'published': published,
                    'thumbnail': thumbnail,
                    'link': link
                })

    else:
        form = YoutubeForm()

    return render(request, 'dashboard/youtube.html', {'form': form, 'results': results})

def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, f'Todo created from {request.user.username} successfully!')
            return redirect('todo')
        
    else:
        form = TodoForm()
    todo = Todo.objects.filter(user=request.user)
    todo_done = not todo.filter(is_finished=False).exists()
    context = {
        'todo': todo,
        'todo_done': todo_done,
        'form': form,
    }
    return render(request, 'dashboard/todo.html', context)

def update_todo(request, pk=None):
    todo = get_object_or_404(Todo, id=pk, user=request.user)
    todo.is_finished = not todo.is_finished
    todo.save()

    next_page = request.GET.get('next', 'todo')
    return redirect(next_page)


def delete_todo(request, pk=None):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    messages.success(request, f'Todo deleted from {request.user.username} successfully!')
    next_page = request.GET.get('next', 'todo')

    return redirect(next_page)

def books(request):
    result_list = []  # initialize empty list

    if request.method == "POST":
        form = DashboardForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['text']

            # Google Books API request
            url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=10'
            response = requests.get(url)
            data = response.json()

            # build result list
            for item in data.get('items', []):
                volume = item.get('volumeInfo', {})
                result_list.append({
                    'title': volume.get('title', 'No title'),
                    'subtitle': volume.get('subtitle', ''),
                    'authors': ', '.join(volume.get('authors', [])),
                    'description': volume.get('description', 'No description'),
                    'categories': ', '.join(volume.get('categories', [])),
                    'pageCount': volume.get('pageCount', 'N/A'),
                    'thumbnail': volume.get('imageLinks', {}).get('thumbnail', ''),
                    'infoLink': volume.get('infoLink', '#'),
                    'averageRating': volume.get('averageRating', 'N/A'),
                })
    else:
        form = DashboardForm()

    context = {
        'form': form,
        'results': result_list,
    }
    return render(request, 'dashboard/books.html', context)

def dictionary(request):
    result = {}

    if request.method == "POST":
        form = DashboardForm(request.POST)  # use the same form
        if form.is_valid():
            word = form.cleaned_data['text']  # note: still 'text'
            
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()[0]
                phonetics = data.get('phonetics', [{}])
                meanings = data.get('meanings', [{}])
                
                result = {
                    'word': data.get('word', word),
                    'phonetic': phonetics[0].get('text', '') if phonetics else '',
                    'audio': phonetics[0].get('audio', '') if phonetics else '',
                    'definition': meanings[0].get('definitions', [{}])[0].get('definition', 'No definition'),
                    'example': meanings[0].get('definitions', [{}])[0].get('example', 'No example'),
                    'synonyms': meanings[0].get('definitions', [{}])[0].get('synonyms', []),
                }
            else:
                result = {'error': 'Sorry, API request limit exceeded or word not found.'}
    else:
        form = DashboardForm()

    return render(request, 'dashboard/dictionary.html', {'form': form, 'result': result})

def wiki(request):
    results = []
    api_debug = ""

    if request.method == "POST":
        form = DashboardForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['text']

            url = "https://en.wikipedia.org/w/api.php"
            params = {
                'action': 'query',
                'list': 'search',
                'srsearch': query,
                'format': 'json',
                'utf8': 1,
                'srlimit': 10
            }

            headers = {
                "User-Agent": "StudentStudyPortal/1.0 (https://yourdomain.com; email@example.com)"
            }

            try:
                response = requests.get(url, params=params, headers=headers, timeout=5)
                response.raise_for_status()
                data = response.json()
                search_results = data.get('query', {}).get('search', [])
                for item in search_results:
                    title = item.get('title')
                    snippet = item.get('snippet', '').replace('<span class="searchmatch">', '').replace('</span>', '')
                    link = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
                    results.append({'title': title, 'snippet': snippet, 'link': link})
            except Exception as e:
                api_debug = str(e)
                results = []

    else:
        form = DashboardForm()

    return render(request, 'dashboard/wiki.html', {'form': form, 'results': results, 'api_debug': api_debug})

def conversion(request):
    result = None
    if request.method == "POST":
        form = ConversionForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['input_value']
            conv_type = form.cleaned_data['input_type']

            if conv_type == 'km_to_m':
                result = value * 1000
            elif conv_type == 'm_to_km':
                result = value / 1000
            elif conv_type == 'c_to_f':
                result = (value * 9/5) + 32
            elif conv_type == 'f_to_c':
                result = (value - 32) * 5/9
    else:
        form = ConversionForm()

    context = {
        'form': form,
        'result': result
    }
    return render(request, 'dashboard/conversion.html', context)


def profile(request):
    todos = Todo.objects.filter(user=request.user).order_by('created_at')
    homeworks = Homework.objects.filter(user=request.user).order_by('due')

    context = {
        'todos': todos,
        'homeworks': homeworks,
    }
    return render(request, 'dashboard/profile.html', context)
