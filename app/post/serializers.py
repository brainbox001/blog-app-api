"""
Serializers for post APIs
"""

from rest_framework import serializers
from core.models import Post, ContentImage


class PostSerializer(serializers.ModelSerializer):
    """Serializer for post."""

    class Meta:
        model = Post
        fields = ['id', 'title', 'textfield']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create a recipe."""

        post = Post.objects.create(**validated_data)

        return post

class ContentImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images."""
    class Meta:
        model = ContentImage
        fields = '__all__'
