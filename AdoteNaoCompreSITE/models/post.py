from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    Id = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=30)
    Texto = models.TextField(blank=True)
    DataPublicacao = models.DateTimeField(auto_now=True)
    IdAutor = models.ForeignKey(User)
