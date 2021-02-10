from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.MovieListView.as_view()),
    path('movie/<int:primary_key>/', views.MovieDetailView.as_view()),
    path('review/', views.ReviewCreateView.as_view()),
    path("rating/", views.AddStarRatingView.as_view()),
]
