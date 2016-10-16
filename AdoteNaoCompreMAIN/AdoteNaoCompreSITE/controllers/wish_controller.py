from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from AdoteNaoCompreSITE.models.dog import Dog
from AdoteNaoCompreSITE.models.wish import Wish
from django.contrib.auth.models import User
from datetime import datetime


def create(request):
    message = None
    code = 0


    idCao = request.POST['idCao']
    cao = Dog.objects.get(Id=idCao)
    protetor = User.objects.get(dog=cao)
    interessado = request.user

    # se usuário atual está autenticado
    if interessado.is_authenticated():

        #verifica se o interessado e o protetor são a mesma pessoa
        if(protetor.id == interessado.id):
            code = 0
            message = "Você não pode adotar seu próprio cão."
            
        elif(cao.Interesse == True):
            code = 0
            message = "Já existe interesse para este cão."
        else:
            #registrando o interesse
            interesse = Wish(
                    IdCao = cao,
                    IdProtetor = protetor,
                    IdInteressado = interessado,
                    DataRegistro = datetime.now()
                )
            interesse.save()
        
            #atualizando o interesse no cão
            cao.Interesse = True
            cao.save()

            #populando resposta
            message = 'Interesse registrado com sucesso.'
            code = 1
    
    #se não estiver autenticado
    else:
        message = 'Você deverá realizar o login para registrar interesse'
        code = 2

    #monta JSON de resposta
    to_json = {
        "message": message,
        "code": code
    }

    return JsonResponse(to_json)

def list(request):
    usuario = request.user    
    interesses = Wish.objects.filter(IdInteressado = usuario.id)
    listaLinhas = []
   
    #para cada interesse do usuário
    for i in interesses:
        cao = Dog.objects.get(Id=i.IdCao.Id)
        protetor = User.objects.get(id=i.IdProtetor.id)
        interessado = User.objects.get(id=i.IdInteressado.id)

        #montando DTO para exibição no template
        listaColunas = []
        listaColunas.append(cao.Nome)
        listaColunas.append(cao.Id)
        listaColunas.append(protetor.first_name + ' ' + protetor.last_name)
        listaColunas.append(protetor.id)
        listaColunas.append(interessado.first_name + ' ' + interessado.last_name)            
        listaColunas.append(interessado.id)
        listaColunas.append(i.DataRegistro)

        listaLinhas.append(listaColunas)

    return render(request, 'wish/list.html', {'listaLinhas': listaLinhas})

def delete(request):
    return redirect(wish_controller.list)
