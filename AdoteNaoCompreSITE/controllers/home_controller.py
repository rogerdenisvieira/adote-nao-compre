from django.shortcuts import render

from AdoteNaoCompreSITE.forms import LoginForm
from AdoteNaoCompreSITE.models.dog import Dog
from AdoteNaoCompreSITE.models.post import Post


def index(request):
    posts = Post.objects.all().order_by("DataPublicacao").reverse()
    caes = Dog.objects.all()[:5]
    form = LoginForm()
    return render(request, 'home.html', {'posts': posts, 'form': form, 'caes': caes})
