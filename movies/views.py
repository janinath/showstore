from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.urls import reverse

# Create your views here.
def Home(request):
    all_gen=Genre.objects.all
    context={
        'all_gen':all_gen
    }
    return render(request,'movies/home.html',context)
@login_required
def Actors(request):
    actors=Actor.objects.all()
    context={
        'actors':actors
    }
    return render(request,'movies/actor.html',context)
@login_required
def Movies(request):
    mov=Movie.objects.all()
    context={
        'mov':mov
    }
    return render(request,'movies/movies.html',context)
@login_required
def Directors(request):
    directors=Director.objects.all()
    context={
        'directors':directors
    }
    return render(request,'movies/director.html',context)
@login_required
def Genres(request):
    geners=Genre.objects.all()
    context={
        'geners':geners
    }
    return render(request,'movies/genre.html',context)
@login_required
def gener_view(request,gid):
    single_gen=Genre.objects.get(id=gid)
    movie_acc_gen=Movie.objects.filter(genre=single_gen)
    context={
        'mov':movie_acc_gen
    }
    return render(request,'movies/movies.html',context)
@login_required
def single_actor(request,aid):
    one_actor=Actor.objects.get(id=aid)
    actor_movies=Movie.objects.filter(actors=one_actor)
    context={
        'one_person':one_actor,
        'mov':actor_movies
    }
    return render(request,'movies/movies.html',context)
@login_required
def director_data(request,did):
    one_dir=Director.objects.get(id=did)
    dir_movies=Movie.objects.filter(director=one_dir)
    context={
        'one_dir':one_dir,
        'mov':dir_movies
    }
    return render(request,'movies/movies.html',context)
@login_required
def movie_desc(request,mid):
    one_movie=Movie.objects.get(id=mid)
    context = {
        'one_movie' : one_movie
    }
    return render(request,'movies/moviepage.html',context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('movies:home')  # Redirect to the home page after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'movies/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully.')
            return redirect('movies:home')  # Redirect to home page after successful registration
    else:
        form = UserRegisterForm()
    return render(request, 'movies/register.html', {'form': form})
def logout_view(request):
    # This will log the user out
    logout(request)
    
    # Redirect to home page after logout
    return redirect(reverse('movies:home'))