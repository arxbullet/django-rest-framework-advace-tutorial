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

    def test_new_user_email_normalized(self):
        """Testea email para nuevo usuario personalizado"""
        email = 'test@mail.com'
        user = get_user_model().objects.create_user(
            email = email,
            password = 'testpass123'
        )
        self.assertEqual(user.email, email.lower)

    def test_new_user_invalid_email(self):
        """nuevo usuario email invalido"""
        with self.assertRaises(ValueError):
            #ejecuta este codigo y si no funciona, arroja error
            get_user_model().objects.create_user(email = None, password = 'Testpass123')

    def test_create_new_superuser(self):
        """probar super usuario creado"""
        email = 'test@mail.com'
        user = get_user_model().objects.create_user(
            email = email,
            password = 'testpass123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
   
    def test_create_new_superuser(self) :
        """  Probar super usuario creado"""
        email='testedatadosis.com'
        password="Testpass123"
        user= get_user_model().objects.create_user(
            email = email,
            password= password)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)



