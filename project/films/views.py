from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, Movie
from .forms import MovieForm

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        "movies": movies,
        "genres": genres,
        "title": "Asosiy Sahifa"
    }
    return render(request, 'films/index.html', context=context)


def movies_by_genre(request, genre_id: int):
    genre = Genre.objects.get(id=genre_id)
    movies = Movie.objects.filter(genre_id=genre_id)
    genres = Genre.objects.all()
    context = {
        "movies": movies,
        "genres": genres,
        "title": genre.name
    }
    return render(request, 'films/index.html', context=context)


def movie_detail(request, movie_id: int):
    movie = Movie.objects.get(pk=movie_id)
    movie.views += 1
    movie.save()
    context = {
        "movie": movie,
        "title": movie.title
    }
    return render(request, 'films/detail.html', context)


def add_movie(request: HttpRequest):
    if request.user.is_staff:
        if request.method == "POST":
            form = MovieForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                movie = form.save()
                return redirect("detail", movie.pk)
        else:
            form = MovieForm()

        context = {
            "form": form,
            "title": "Kino qo'shish"
        }
        return render(request, 'films/add_movie.html', context)
    else:
        return render(request, '404.html')


def delete_movie(request, pk: int):
    if request.user.is_staff:
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
    return redirect('index')