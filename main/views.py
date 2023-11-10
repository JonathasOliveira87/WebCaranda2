from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from panelUser.models import profileManager

def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    
    else:
        if request.user.is_authenticated:
            messages.warning(request, 'Você já está logado!')
            return redirect('/')

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if username == "" or email == "" or password == "" or confirmPassword == "":
            messages.error(request, 'Não deixe campos vazios!')
            return redirect('/')

        new_user = User.objects.filter(username=username)

        if new_user.exists():
            messages.info(request, 'Nome de usuário já existe!')
            return redirect('/')
        
        if password != confirmPassword:
            messages.info(request, 'As senhas não conferem!')
            return redirect('/')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()

        sem_info = 'Sem Informações'
        # Crie um profileManager para o novo usuário
        new_profile = profileManager(user=new_user, telefone=sem_info, morador=sem_info, dono=sem_info, casa=0, carro=sem_info, moto=sem_info, pet=sem_info)
        new_profile.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('/')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            if user is not None and user.check_password(password):
                login(request, user)
                messages.success(request, 'Logado com sucesso!')
                return redirect('/')
            else:
                messages.error(request, 'Nome de usuário ou senha incorretos.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

    return redirect('/')


@login_required 
def logout_user(request):
    logout(request)
    messages.success(request, 'Usuário deslogado com sucesso!')
    return redirect('/')