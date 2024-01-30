"""
Tests for models.
"""
from unittest.mock import patch
from django.test import TestCase

from django.contrib.auth import get_user_model
from core import models


def create_user(email='user@example.com', first_name='Dan', last_name='Marc', username='Brainbox', is_active=True, password='testpass123'):
    """Create a return a new user."""
    return get_user_model().objects.create_user(email, first_name, last_name, username, is_active, password)


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email='user@example.com'
        first_name='Dan'
        last_name='Marc'
        username='Brainbox'
        is_active=True
        password='testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            username=username,
            is_active= is_active,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_without_incomplete_details(self):
        """Test that creating a user without incomplete details raises a ValueError."""
        with self.assertRaises(ValueError):
          get_user_model().objects.create_user(
          email='user@example.com',
          first_name='Dan',
          last_name='Marc',
          is_active=True,
          password='testpass123'
          )
