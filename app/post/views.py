"""
Views for the post APIs
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Post, Content, ContentImage
from .serializers import PostSerializer, ContentSerializer, ContentImageSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        post_data = request.data.copy()
        print(f'####post = {type(post_data)}')
        print(f'####post = {request.data}')
        content = post_data.pop('content', None)
        print(f'####content11 = {content}')
        content_data = post_data.pop('content.textfield', None)[0]
        content_data_dict = {'content': content_data,
                             'textfield': content_data
        }
        print(f'####content = {content_data_dict}')
        post_serializer = PostSerializer(data=post_data)
        content_serializer = ContentSerializer(data=content_data_dict)

        if content_serializer.is_valid(raise_exception=True):
            if post_serializer.is_valid(raise_exception=True):
                content_instance = content_serializer.save(author=request.user)
                post_instance = post_serializer.save(author=request.user, content=content_instance)

                return Response(PostSerializer(post_instance).data, status=status.HTTP_201_CREATED)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ContentImageViewSet(ModelViewSet):
    queryset = ContentImage.objects.all()
    serializer_class = ContentImageSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        data['uploader_id'] = request.user.id
        serialized = ContentImageSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]
