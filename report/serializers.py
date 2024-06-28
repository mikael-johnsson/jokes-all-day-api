from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    """
    """
    author = serializers.ReadOnlyField(source='author.username')
    joke_title = serializers.ReadOnlyField(source='joke.title')

    def to_representation(self, obj):
        readableName = super().to_representation(obj)
        readableName['reason'] = readableName['reason'].replace("_", " ")
        return readableName
    
    def to_internal_value(self, data):
        internalName = super().to_representation(data)
        internalName['reason'] = internalName['reason'].replace(" ", "_")
        return internalName

    class Meta:
        model = Report
        fields = [
            'id', 'author', 'joke', 'joke_title', 'reason', 'content', 'created_at',
            'handled', 
        ]