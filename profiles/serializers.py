from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    """
    Reorganize data to fit JSON
    get_is_owner checks if the user making the request is
    the owner of the requested object
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    jokes_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    followed_count = serializers.ReadOnlyField()
    given_rating = serializers.ReadOnlyField()
    received_rating = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'name', 'is_owner',
            'following_id', 'jokes_count', 'followers_count',
            'followed_count', 'given_rating', 'received_rating'
            ]