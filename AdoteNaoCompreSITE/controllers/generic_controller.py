from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render


# Create your views here.


@permission_required('adotenaocompre.restricted', raise_exception=True)
def restricted(request):
    return render(request, 'restricted.html')


def unauthorized_handler(request):
    messages.warning(request, "Voce nao tem permissao para acessar a pagina solicitada.", extra_tags='alert-danger')
    return render(request, 'home.html', {})


def pageNotFoundHandler(request):
    return render(request, '404.html', {})
