"""
Serializers for post APIs
"""

from rest_framework import serializers
from core.models import Post, Content, ContentImage


class ContentSerializer(serializers.ModelSerializer):
    """Serializer for post contents."""
    class Meta:
        model = Content
        fields = ['id', 'textfield']
        read_only_fields = ['id']

class PostSerializer(serializers.ModelSerializer):
    """Serializer for post."""
    content = ContentSerializer(required=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content']
        read_only_fields = ['id']

class ContentImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images."""
    class Meta:
        model = ContentImage
        fields = '__all__'
