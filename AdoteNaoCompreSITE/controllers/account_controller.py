from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from AdoteNaoCompreSITE.controllers import home_controller, account_controller
from AdoteNaoCompreSITE.forms import LoginForm
from AdoteNaoCompreSITE.models.user_extras import User_extras


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # verifica se o usuário existe
        if User.objects.filter(username=username).exists():

            # guarda o usuário que está tentando entrar
            user_to_lock = User.objects.get(username=request.POST['username'])

            # retorna as informações extras do usuário
            extra = User_extras.objects.get(IdPai=user_to_lock)

            # verifica se a contagem é menos que a do arquivo de configuração
            if extra.Tentativas < getattr(settings, "TENTATIVAS_LOGIN", None):

                # tenta autenticar
                user = authenticate(username=username, password=password)

                # se o usuário foi autenticado
                if user is not None:
                    # se o usuário está ativo
                    if user.is_active:
                        login(request, user)
                        messages.success(request, 'Seja bem-vindo ' + user.username, extra_tags='alert-success')
                        return redirect(home_controller.index)
                    else:
                        message = 'Usuário inativo.'
                else:
                    message = 'Falha na autenticação.'
                    extra.Tentativas += 1
                    extra.save()
            else:
                message = 'Seu usuário foi bloqueado. Entre em contato com o administrador.'
        else:
            message = 'Usuário inválido'

        # devolve a página de login com as messages
        messages.warning(request, message, extra_tags='alert-warning')
        return redirect(account_controller.login_user)

    form = LoginForm
    return render(request, 'login.html', {'LoginForm': form})


def logout_user(request):
    messages.success(request, 'Logout realizado com sucesso.', extra_tags='alert-success')
    logout(request)
    return redirect(home_controller.index)
