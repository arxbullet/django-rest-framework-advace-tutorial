from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    """probar crear un nuevo usuario con un email correctamente"""
    def test_create_user_with_email_succesfull(self):
        email = 'test@mail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))