from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomLoginForm
from .forms import CustomUserCreationForm

def index_view(request):
    return render(request, 'autenticacao/index.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = CustomLoginForm()
    return render(request, 'autenticacao/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('login')

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login') 
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, 'autenticacao/register.html', {'form': form})
@login_required
def home_view(request):
    return render(request, 'autenticacao/home.html')
