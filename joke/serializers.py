from rest_framework import serializers
from .models import Joke

class JokeSerializer(serializers.ModelSerializer):
    """
    get_is_owner validates if the request user is the owner of the Joke (object)
    """
    author = serializers.ReadOnlyField(source='author.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Joke
        fields = [
            'id', 'author', 'title', 'content', 'created_at', 'is_owner'
        ]