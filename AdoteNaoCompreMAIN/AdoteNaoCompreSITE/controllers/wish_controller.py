from django.http import JsonResponse
from django.core import serializers
from AdoteNaoCompreSITE.models.dog import Dog

def check_wishlist(request):
    data = serializers.serialize("json", Dog.objects.all())

    to_json = {
        "key1": "value1",
        "key2": "value2"
    }
    return JsonResponse(data, safe=False)
