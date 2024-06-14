from django.urls import path
from joke import views

urlpatterns = [
    path('jokes/', views.JokeList.as_view()),
    path('jokes/<int:pk>', views.JokeDetail.as_view()),
]