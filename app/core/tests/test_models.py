from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        """Test Creating a user succesfully with email"""
        email = "test@test.com"
        password = "test_pass"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password), password)

    def test_new_user_email_normalized(self):
        """Test email is normalized"""
        email = "test@EMAIL.com"
        user = get_user_model().objects.create_user(email, password="abcd")
        self.assertEqual(user.email, email.lower())

    def test_ivalid_email_new_user(self):
        """Invalid email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            "testsuper@email.com", password="abcd21"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
