from django.shortcuts import render, redirect, get_object_or_404
from AdoteNaoCompreSITE.models.dog import Dog
from AdoteNaoCompreSITE.models.breed import Breed
from AdoteNaoCompreSITE.forms import DogForm, SearchDogForm
from AdoteNaoCompreSITE.controllers import home_controller, dog_controller
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime


def search(request):
    key = request.POST['key']
    dogs = Dog.objects.filter(Nome__icontains=key) | Dog.objects.filter(Info__icontains=key)
    print('passei aqui')
    print(key)
    return render(request, 'search.html', {'caes': dogs})


# se GET = retorna a pagina de criacao
# se POST = valida e persiste o objeto
@login_required
def create(request):
    if request.method == 'POST':
        # popula o form com os dados do client
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.IdProtetor = request.user
            dog.Nome = request.POST['Nome']
            dog.IdRaca.Id = request.POST['IdRaca']
            dog.Info = request.POST['Info']
            dog.Foto = request.FILES['Foto']
            dog.Idade = request.POST['Idade']
            dog.Sexo = request.POST['Sexo']
            dog.DataRegistro = datetime.now()
            dog.save()

            print('validado')
            return redirect(home_controller.index)
        else:
            print(form.errors)
    else:
        form = DogForm()
    # devolve o form a pagina com o validation summary
    return render(request, 'dog/create.html', {'DogForm': form})


@login_required
def edit(request, id):
    dog = get_object_or_404(Dog, Id=id)
    if request.method == "POST":
        print("este foi um POST")
        form = DogForm(request.POST, request.FILES, instance=dog)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.IdProtetor = request.user
            dog.Nome = request.POST['Nome']
            dog.Info = request.POST['Info']
            dog.Foto = request.FILES['Foto']
            dog.Idade = request.POST['Idade']
            dog.Sexo = request.POST['Sexo']
            dog.save()
            return redirect(home_controller.index)
    else:
        print("este foi um GET")
        form = DogForm(instance=dog)
    return render(request, 'dog/edit.html', {'DogForm': form, 'dog': dog})


@login_required
def list(request):
    user = request.user
    if user.is_authenticated():
        caes = Dog.objects.filter(IdProtetor=request.user)
        return render(request, 'dog/list.html', {'user': user, 'caes': caes})


def show(request,id):
    dog = get_object_or_404(Dog, Id=id)
    owner = User.objects.get(dog=dog)
    breed = Breed.objects.get(dog=dog)

    dto = {
            'Nome': dog.Nome,
            'Idade': dog.Idade,
            'Informação': dog.Info,
            'Interesse' : dog.Interesse,
            'Sexo': dog.Sexo,
            'Data de Registro': dog.DataRegistro,
            'Raça': breed.Info
        }

    foto_url = dog.Foto

    return render(request, 'dog/show.html', {'dto': dto.items(), 'owner': owner, 'dog': dog})


@login_required
def delete(request):
    user = request.user   
    id = request.POST["id"]
    if user.is_authenticated():
        print(id)
        Dog.objects.filter(Id=id).delete()
        caes = Dog.objects.filter(IdProtetor=request.user)
        return redirect(dog_controller.list)