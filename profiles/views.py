from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from jokes.permissions import IsOwnerOrReadOnly

class ProfileList(APIView):
    """
    List all profiles
    No create view as profile creation is handled by django signals (in the Profiles model)
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles, 
            many=True, 
            context = {'request': request})

        return Response(serializer.data)

class ProfileDetail(APIView):
    """
    Display one profile
    get_object sees if it exists
    get returns the serialized data
    put updates the serializer with data from the request
    serializer_class tells REST what fields are in the model 
    (to show in the mock "frontend")
    permission_classes tells REST which users have 
    access to what profile functions
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except:
            raise Http404
    

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, 
            context = {'request': request})
        return Response(serializer.data)


    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, 
            data=request.data, 
            context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)