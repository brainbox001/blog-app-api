"""
Views for the user API.
"""
from .tasks import send_verification_email
from rest_framework import generics, views
from user.serializers import (
    UserSerializer,

    )


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_verification_email.delay(user.email)

