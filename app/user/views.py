"""
Views for the user API.
"""
from core.models import User
from .tasks import send_verification_email
from rest_framework import generics, views
from user.serializers import (
    UserSerializer,
    )
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        user = serializer.save()
        send_verification_email.delay(user.email)

