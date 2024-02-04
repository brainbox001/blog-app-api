"""
Views for the post APIs
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Post, ContentImage
from .serializers import PostSerializer, ContentImageSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from .permissions import IsOwnerOrReadOnly

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request):
        """Returns the list of post."""
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        print(request.META.get('HTTP_HOST'))
        return Response(serializer.data)

    def perform_create(self, serializer):
        """Create a new post"""
        serializer.save(author=self.request.user)


class ContentImageViewSet(ModelViewSet):
    queryset = ContentImage.objects.all()
    serializer_class = ContentImageSerializer
    permission_classes = [IsAdminUser, IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        data = request.data

        serialized = ContentImageSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsAdminUser, IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]
