from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm, LoginForm
from .models import User

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'autenticacao/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'autenticacao/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def cadastro_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UserForm()
    return render(request, 'autenticacao/cadastro_usuario.html', {'form': form})

@login_required
def detalhes_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    return render(request, 'autenticacao/detalhes_usuario.html', {'usuario': usuario})