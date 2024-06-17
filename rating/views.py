from rest_framework import generics, permissions
from jokes_main.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer

class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    
    """
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()
