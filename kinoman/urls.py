from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.MovieListView.as_view()),
    path('movie/<int:pk>/', views.MovieDetailView.as_view()),
    path('review/', views.ReviewCreateView.as_view()),
    path("rating/", views.AddStarRatingView.as_view()),
    path("actors/", views.ActorsListView.as_view()),
    path("actor/<int:pk>/", views.ActorsDetailView.as_view()),
]
