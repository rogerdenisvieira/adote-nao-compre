from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.core import serializers
from AdoteNaoCompreSITE.models.dog import Dog
from django.contrib.auth.models import User

def check_wishlist(request):
    data = serializers.serialize("json", Dog.objects.all())

    to_json = {
        "key1": "value1",
        "key2": "value2"
    }
    return JsonResponse(data, safe=False)

def create(request):
    idCao = request.POST['idCao']
    cao = Dog.objects.get(Id=idCao)
    protetor = User.objects.get(dog=cao)
    interessado = request.user

    to_json = {
            'message':'Teste de registro de interesse'          
        }
    print(to_json)
    #return JsonResponse(to_json, safe=False)
    return HttpResponse(json.dumps(to_json), content_type='application/json')

