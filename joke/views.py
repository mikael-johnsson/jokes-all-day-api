from django.http import Http404
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Joke
from .serializers import JokeSerializer
from jokes_main.permissions import IsOwnerOrReadOnly

class JokeList(generics.ListCreateAPIView):
    """
    get returns all jokes after they've been serialized
    """
    serializer_class = JokeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Joke.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class JokeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Display one Joke
    # get_object sees if it exists
    # get returns the serialized data
    # put updates the serializer with data from the request
    # serializer_class tells REST what fields are in the model 
    # (to show in the mock "frontend")
    # permission_classes tells REST which users have 
    # access to what joke functions
    """

    serializer_class = JokeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Joke.objects.all()
