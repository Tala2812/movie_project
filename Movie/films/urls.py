from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_movie, name='add_movie'),
    path('list/', views.list_movies, name='list_movies'),
    path('cards/', views.card_view, name='card_view'),
]