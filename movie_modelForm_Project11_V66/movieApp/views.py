from django.shortcuts import render
from movieApp.forms import MovieForm
from movieApp.models import Movies

# Create your views here.
def index_view(request):
    return render(request,"templates/index.html")

def add_movie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request,"templates/addMovie.html",{'form':form})

def list_movie_view(request):
    movie_list = Movies.objects.all()
    return render(request,"templates/listMovie.html",{'movie_list':movie_list})