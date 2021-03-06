from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'testApp/index.html')


def movies_view(request):
    return render(request,'testApp/movies.html')


def sports_view(request):
    return render(request,'testApp/sports.html')


def politics_view(request):
    return render(request,'testApp/politics.html')