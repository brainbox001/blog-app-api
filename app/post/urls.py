"""
URL mappings for the post app.
"""

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from post.views import PostViewSet, ContentImageViewSet

router = SimpleRouter()
router.register('post', PostViewSet)
router.register('image', ContentImageViewSet)

app_name = 'post'

urlpatterns = [
    path('', include(router.urls)),
]
