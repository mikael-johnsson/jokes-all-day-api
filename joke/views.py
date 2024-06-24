from django.db.models import Count, Avg
from rest_framework import permissions, generics, filters
from .models import Joke
from .serializers import JokeSerializer
from jokes_main.permissions import IsOwnerOrReadOnly

class JokeList(generics.ListCreateAPIView):
    """
    get returns all jokes after they've been serialized
    """
    serializer_class = JokeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Joke.objects.annotate(
        rating_count = Count('rating', distinct=True),
        average_rating = Avg('rating__rating')
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter
    ]

    ordering_fields = [
        'rating_count',
        'average_rating'
    ]

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
    queryset = Joke.objects.annotate(
        rating_count = Count('rating'),
        average_rating = Avg('rating__rating')
    ).order_by('-created_at')
