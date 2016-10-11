from django.shortcuts import render, redirect, get_object_or_404
from AdoteNaoCompreSITE.models.dog import Dog
from AdoteNaoCompreSITE.forms import DogForm, SearchDogForm
from AdoteNaoCompreSITE.controllers import home_controller, dog_controller
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def search(request):
    dogs = Dog.objects.all()
    form = SearchDogForm()
    return render(request, 'search.html', {'caes': dogs, 'form': form})


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
            dog.Info = request.POST['Info']
            dog.Foto = request.FILES['Foto']
            dog.Idade = request.POST['Idade']
            dog.Sexo = request.POST['Sexo']
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
    form = DogForm(instance=dog)
    owner = User.objects.get(dog=dog)
    return render(request, 'dog/show.html', {'DogForm': form, 'dog': dog, 'owner': owner})

@login_required
def delete(request):
    print("passou pelo delete")
    user = request.user   
    id = request.POST["id"]
    if user.is_authenticated():
        print(id)
        Dog.objects.filter(Id=id).delete()
        caes = Dog.objects.filter(IdProtetor=request.user)
        return redirect(dog_controller.list)