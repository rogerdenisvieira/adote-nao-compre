from django.shortcuts import render
from AdoteNaoCompreSITE.forms import UserForm
from django.contrib.auth.decorators import login_required
from AdoteNaoCompreSITE.models.dog import Dog
from django.contrib.auth.models import User


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
def show_profile(request):
    user = request.user
    if user.is_authenticated():
        caes = Dog.objects.filter(IdProtetor=request.user)
        dto = {
                'Nome': user.first_name + ' ' + user.last_name
            }
        return render(request, 'user/profile.html', {'dto': dto.items(), 'caes': caes})

def show(request, id):
    user = User.objects.filter(id=id)
    return render(request, 'user/show.html', {'user': user})
