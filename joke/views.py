from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Joke
from .serializers import JokeSerializer

class JokeList(APIView):
    """
    get returns all jokes after they've been serialized
    """
    serializer_class = JokeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

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