from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, Category, Actor
from .forms import ReviewForm


class MoviesView(ListView):
    """MoviesView"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"


class MovieDetailView(DetailView):
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


class ActorView(DetailView):
    """ Information about actor """
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = "name"
