from rest_framework import serializers

from .models import Story

class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'body', 'created_at', 'author')
        model = Story