from django.urls import path
from .views import index, movies_by_genre, movie_detail, add_movie, delete_movie

urlpatterns = [
    path('', index, name="index"),
    path('movie/add/', add_movie, name="add_movie"),
    path('movie/delete/<int:pk>', delete_movie, name="delete_movie"),
    path('genre/<int:genre_id>/', movies_by_genre, name="by_genre"),
    path('movie/<int:movie_id>/', movie_detail, name="detail"),
]