from django.shortcuts import render
from django.views import generic
from . models import Movie 
# Create your views here.

class HoumeListView(generic.ListView):
    model = Movie
    template_name = 'index.html'
    context_object_name = 'home'


class SingleListView(generic.ListView):
    model = Movie 
    template_name = 'single.html'
    content_object_name = 'single'

class MovieListView(generic.ListView):
    model = Movie
    template_name = 'movie.html'
    context_object_name = 'movie'