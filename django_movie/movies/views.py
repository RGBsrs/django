from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, Actor, Genre
from .forms import ReviewForm


class GenreYear:
    """Years and genres of films"""

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MoviesView(GenreYear, ListView):
    """MoviesView"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"


class MovieDetailView(GenreYear, DetailView):
    # Detailed view
    model = Movie
    slug_field = 'url'
    template_name = "movies/moviesingle.html"


class AddReview(View):
    """Add Review"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(GenreYear, DetailView):
    """ Information about actor """
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = "name"


class FilterMoviesView(GenreYear, ListView):
    """Film filter"""

    def get_queryset(self):
        queryset = Movie.objects.filter(
            year__in=self.request.GET.getlist("year"), genres__in=self.request.GET.getlist("genres"))
        return queryset
