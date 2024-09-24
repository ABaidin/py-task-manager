from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager_app.models import Position

User = get_user_model()


class AccountsViewsTest(TestCase):

    def setUp(self):
        position = Position.objects.create(name="Developer")
        self.user = User.objects.create_user(
            username='john',
            password='password123',
            position=position
        )

    def test_login_view_uses_correct_template(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_register_view_uses_correct_template(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
