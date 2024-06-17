from django.db import IntegrityError
from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    """
    Rating serializer
    """
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Rating
        fields = [
            'author', 'joke', 'created_at', 'rating',
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'message': 'possible duplicate'
            })

