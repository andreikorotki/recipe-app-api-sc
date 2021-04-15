from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test create a new user successfull"""
        email = 'test@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_email_unsuccessful_password(self):
        """Test create a new user and try to check wrong password"""
        email = 'test1@gmail.com'
        password = 'Testpass123'
        wrong_password = 'wrongTestpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertFalse(user.check_password(wrong_password))

    def test_new_user_email_normalized(self):
        """Test insensitive user email"""
        email = 'test4@GMAiL.Com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that invalid emails are not accepted"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')


    def test_create_new_superuser(self):
        """Test new super user"""
        user = get_user_model().objects.create_superuser('test@mail.ru',
                                                         '1111112aZ')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

