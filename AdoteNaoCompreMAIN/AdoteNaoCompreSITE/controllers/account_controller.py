from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    print('efetuando login...')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Seja bem-vindo ' + user.username, extra_tags='alert-success')
                return render(request, 'home.html', {})
            else:
                messages.warning(request, 'Usuario inativo.', extra_tags='alert-warning')
                return render(request, 'home.html', {})
        else:
            messages.warning(request, 'Usuario ou senha invalidos.', extra_tags='alert-warning')
            return render(request, 'home.html', {})


def logout_user(request):
    messages.success(request, 'Logout realizado com sucesso.', extra_tags='alert-success')
    logout(request)
    return render(request, 'home.html', {})
