from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminsiteTests(TestCase):
    def setup(self):
        self.client =  Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='adminedatadosis.com',
            password= 'password123')

        self.client.force_login(self.admin_user)

        self.user =  get_user_model().objects.create_user(
            email = 'testedatadosis.com',
            password= 'pass123',
            name ="Test user nombre completo")

    def test_users_listed(self):
        """Testear oue Los usuarios han sido enlistados en La pagina de usuario"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """ Prueba que La pagina editada por el usuario funcione"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        #que es reverse ? :allows to retrieve url details from url's.py file through the name value provided there
        res = self.client.get(url)                                    
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Prueba que La pagina de crear usuario funcione"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)                               
        self.assertEqual(res.status_code, 200)