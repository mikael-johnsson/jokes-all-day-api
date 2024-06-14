from django.urls import path
from joke import views

urlpatterns = [
    path('jokes/', views.JokeList.as_view())
]