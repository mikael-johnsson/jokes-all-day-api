from django.db.models import Count, Avg
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from jokes_main.permissions import IsProfileOwnerOrReadOnly

class ProfileList(generics.ListAPIView):
    """
    List all profiles
    No create view as profile creation is handled by django signals (in the Profiles model)
    Annotate allows the user to add fields to filtering
    distinct makes sure there are no duplicates in the filtering
    """
    queryset = Profile.objects.annotate(
        jokes_count = Count('owner__joke', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True),
        given_rating = Avg('owner__rating__rating'),
        received_rating = Avg('owner__joke__rating__rating')   
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter
    ]

    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]

    ordering_filters = [
        'jokes_count',
        'followers_count',
        'following_count',
        'received_rating',
        'given_rating',
    ]

    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Display one profile
    # get_object sees if it exists
    # get returns the serialized data
    # put updates the serializer with data from the request
    # serializer_class tells REST what fields are in the model 
    # (to show in the mock "frontend")
    # permission_classes tells REST which users have 
    # access to what profile functions
    """
    permission_classes = [IsProfileOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        jokes_count = Count('owner__joke', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True),
        given_rating = Avg('owner__rating__rating'),
        received_rating = Avg('owner__joke__rating__rating')   
    ).order_by('-created_at')

    serializer_class = ProfileSerializer
