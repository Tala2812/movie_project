from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def index(request):
    return render(request, 'films/index.html')

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_movies')  # Redirect to list_movies after adding
    else:
        form = MovieForm()
    return render(request, 'films/add_movie.html', {'form': form})

def list_movies(request):
    movies = Movie.objects.all()
    return render(request, 'films/list_movies.html', {'movies': movies})

def card_view(request):
    movies = Movie.objects.all()
    return render(request, 'films/card_view.html', {'movies': movies})