from django.shortcuts import render
from AdoteNaoCompreSITE.forms import UserForm
from django.contrib.auth.decorators import login_required
from AdoteNaoCompreSITE.models.dog import Dog


def create(request):
    # se for POST, o usuario esta sendo criado
    if request.method == 'POST':
        form = UserForm()
        print('This is a POST to create an user.')
        return render(request, 'user/create.html', {'UserForm': form})
    # se for GET, devolve a pagina de criação do usuario
    else:
        print('Retrieving user creation forms')
        form = UserForm()
        return render(request, 'user/create.html', {'UserForm': form})


@login_required
def show(request):
    user = request.user
    if user.is_authenticated():
        caes = Dog.objects.filter(IdProtetor=request.user)
        return render(request, 'user/show.html', {'user': user, 'caes': caes})
