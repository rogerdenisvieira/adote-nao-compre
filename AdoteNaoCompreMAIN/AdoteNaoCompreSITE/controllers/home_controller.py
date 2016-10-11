from django.shortcuts import render
from AdoteNaoCompreSITE.models.post import Post
from AdoteNaoCompreSITE.models.dog import Dog
from AdoteNaoCompreSITE.forms import LoginForm


def index(request):
    posts = Post.objects.all().order_by("DataPublicacao").reverse()
    caes = Dog.objects.all()
    form = LoginForm()
    return render(request, 'home.html', {'posts': posts, 'form': form, 'caes': caes})
