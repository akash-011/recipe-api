from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test Creating a user succesfully with email"""
        email = "test@test.com"
        password = "test_pass"
        user = get_user_model.objects.user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password), password)
