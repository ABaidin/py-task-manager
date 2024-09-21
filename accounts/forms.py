from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = [
            "username", "password1", "password2",
            "email", "first_name", "last_name"
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=True)
