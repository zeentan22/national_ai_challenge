from django.urls import path
from . import views


urlpatterns = [
    path("", views.SentimentListCreateAPIView.as_view(), name="sentiment-list"),
    path("<int:pk>/", views.SentimentDetailAPIView.as_view(), name="sentiment-detail"),
    path("<int:pk>/update/", views.SentimentUpdateAPIView.as_view(), name="sentiment-update"),
    path("<int:pk>/delete/", views.SentimentDeleteAPIView.as_view(), name="sentiment-delete"),
]
