from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from captcha.fields import CaptchaField

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2') 

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class CustomLoginForm(AuthenticationForm):
    captcha = CaptchaField()
    username = forms.CharField(label='Nome de usuário', max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))
