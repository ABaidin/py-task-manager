from django.test import TestCase
from accounts.forms import RegistrationForm, LoginForm
from django.contrib.auth import get_user_model
from task_manager_app.models import Position, Employee

User = get_user_model()

class RegistrationFormTest(TestCase):

    def setUp(self):
        self.position = Position.objects.create(name="Developer")

    def test_registration_form_placeholders(self):
        form = RegistrationForm()
        self.assertEqual(form.fields['username'].widget.attrs.get('placeholder'), None)
        self.assertEqual(form.fields['email'].label, "Email address")

    def test_valid_registration_form(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'position': self.position.id
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_registration_form(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'mismatch',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'position': self.position.id
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

class LoginFormTest(TestCase):

    def test_login_form_remember_me_checkbox(self):
        position = Position.objects.create(name="Developer")
        Employee.objects.create_user(
            username="testuser",
            password="testpassword123",
            position=position
        )
        form_data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'remember_me': True
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['remember_me'], True)
