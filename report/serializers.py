from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    """
    """
    author = serializers.ReadOnlyField(source='author.username')
    joke_title = serializers.ReadOnlyField(source='joke.title')

    class Meta:
        model = Report
        fields = [
            'id', 'author', 'joke', 'joke_title', 'reason', 'content', 'created_at',
            'handled', 
        ]