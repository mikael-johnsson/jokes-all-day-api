from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Joke
from .serializers import JokeSerializer
from jokes_main.permissions import IsOwnerOrReadOnly

class JokeList(APIView):
    """
    get returns all jokes after they've been serialized
    """
    serializer_class = JokeSerializer
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly
    # ]

    def get(self, request):
        jokes = Joke.objects.all()
        serializer = JokeSerializer(
            jokes, many=True, context={'request': request}
        )
        return Response(serializer.data)
    

    def post(self, request):
        serializer = JokeSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(author = request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

class JokeDetail(APIView):
    """
    Display one Joke
    get_object sees if it exists
    get returns the serialized data
    put updates the serializer with data from the request
    serializer_class tells REST what fields are in the model 
    (to show in the mock "frontend")
    permission_classes tells REST which users have 
    access to what joke functions
    """

    serializer_class = JokeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            joke = Joke.objects.get(pk=pk)
            self.check_object_permissions(self.request, joke)
            return joke
        except Joke.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        joke = self.get_object(pk)
        serializer = JokeSerializer(
            joke, context={'request': request}
            )
        return Response(serializer.data)

    def put(self, request, pk):
        joke = self.get_object(pk)
        serializer = JokeSerializer(
            joke, data=request.data, context={'request': request} 
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data
                )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
    
    def delete(self, request, pk):
        joke = self.get_object(pk)
        joke.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )