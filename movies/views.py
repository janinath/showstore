from django.shortcuts import render
from . models import *
# Create your views here.
def Home(request):
    all_gen=Genre.objects.all
    context={
        'all_gen':all_gen
    }
    return render(request,'movies/home.html',context)

def Actors(request):
    actors=Actor.objects.all()
    context={
        'actors':actors
    }
    return render(request,'movies/actor.html',context)

def Movies(request):
    mov=Movie.objects.all()
    context={
        'mov':mov
    }
    return render(request,'movies/movies.html',context)

def Directors(request):
    directors=Director.objects.all()
    context={
        'directors':directors
    }
    return render(request,'movies/director.html',context)

def Genres(request):
    geners=Genre.objects.all()
    context={
        'geners':geners
    }
    return render(request,'movies/genre.html',context)

def gener_view(request,gid):
    single_gen=Genre.objects.get(id=gid)
    movie_acc_gen=Movie.objects.filter(genre=single_gen)
    context={
        'mov':movie_acc_gen
    }
    return render(request,'movies/movies.html',context)
def single_actor(request,aid):
    one_actor=Actor.objects.get(id=aid)
    actor_movies=Movie.objects.filter(actors=one_actor)
    context={
        'one_person':one_actor,
        'mov':actor_movies
    }
    return render(request,'movies/movies.html',context)
def director_data(request,did):
    one_dir=Director.objects.get(id=did)
    dir_movies=Movie.objects.filter(director=one_dir)
    context={
        'one_dir':one_dir,
        'mov':dir_movies
    }
    return render(request,'movies/movies.html',context)
def movie_desc(request,mid):
    return render(request,'movies/moviepage.html')