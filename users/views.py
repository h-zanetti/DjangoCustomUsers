from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            messages.success(request, 'Usuário registrado com sucesso')
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    context = {
        'title': 'Registro',
        'form': form,
    }

    return render(request, 'core/base_forms.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, 'Usuário logado com sucesso')
            return redirect('index')
    else:
        form = AuthenticationForm()

    context = {
        'title': 'Entrar',
        'form': form,
    }

    return render(request, 'core/base_forms.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Usuário desconectado com sucesso')
    return redirect('index')
