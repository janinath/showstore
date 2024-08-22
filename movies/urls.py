from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.urls import path
from . import views
app_name='movies'
urlpatterns=[
    path('',views.Home,name='home'),
    path('actor/',views.Actors,name='actor'),
    path('movies/',views.Movies,name='movie'),
    path('director/',views.Directors,name='director'),
    path('genre/',views.Genres,name='genre'),
    path('gener_view/<int:gid>',views.gener_view,name='gener_view'),
    path('single_actor/<int:aid>',views.single_actor,name='single_actor'),
    path('director_data/<int:did>',views.director_data,name='director_data'),
    path('movie_desc/<int:mid>',views.movie_desc,name='movie_desc'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]