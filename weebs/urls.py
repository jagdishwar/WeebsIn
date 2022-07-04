from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/character/<str:word>', views.by_character, name='character'),
    path('home/anime/<str:anime>', views.by_anime, name='anime_title'),
    ]