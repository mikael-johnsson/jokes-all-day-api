from rest_framework import generics, permissions
from jokes_main.permissions import IsProfileOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    List all Followers
    Create a follower if logged in
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower
    """
    serializer_class = FollowerSerializer
    permission_classes = [IsProfileOwnerOrReadOnly]
    queryset = Follower.objects.all()
