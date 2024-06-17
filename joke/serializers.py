from rest_framework import serializers
from .models import Joke
from rating.models import Rating

class JokeSerializer(serializers.ModelSerializer):
    """
    get_is_owner validates if the request user is the owner of the Joke (object)
    """
    author = serializers.ReadOnlyField(source='author.username')
    is_owner = serializers.SerializerMethodField()
    rating_id = serializers.SerializerMethodField()
    rating_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    def get_rating_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                author=user, joke=obj
            ).first()
            return rating.id if rating else None
        return None

    class Meta:
        model = Joke
        fields = [
            'id', 'author', 'title', 'content', 'created_at',
            'is_owner', 'rating_id', 'rating_count',
        ]