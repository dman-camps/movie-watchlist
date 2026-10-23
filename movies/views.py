from django.shortcuts import render, redirect
from .models import Movie


def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        release_year = request.POST.get('release_year') or None
        genre = request.POST.get('genre', '')
        watched = request.POST.get('watched') == 'on'

        Movie.objects.create(
            title=title,
            release_year=release_year,
            genre=genre,
            watched=watched
        )

        return redirect('home')

    query = request.GET.get('q', '')
    movies = Movie.objects.all().order_by('title')

    if query:
        movies = movies.filter(title__icontains=query)

    return render(request, 'movies/home.html', {
        'movies': movies,
        'query': query
    })