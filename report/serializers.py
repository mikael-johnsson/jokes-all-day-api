from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    """
    """
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Report
        fields = [
            'id', 'author', 'joke', 'content', 'created_at',
            'handled', 'reason', 
        ]