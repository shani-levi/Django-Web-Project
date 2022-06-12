from django.shortcuts import render
from .models import Movie
# Create your views here.
def main_home(request):
    return render(request, 'mainhome.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def movie_list(request):
    movies = Movie.objects.all().order_by('title')
    return render(request, 'movie_list1.html', {'movies': movies})


def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    return render(request, "detail.html", {'movie': movie})



