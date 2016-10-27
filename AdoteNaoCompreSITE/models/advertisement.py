from django.db import models
from django.contrib.auth.models import User


class Advertisement(models.Model):
    """description of class"""
    Id = models.AutoField(primary_key=True)
    Descricao = models.CharField(max_length=100)
    Banner = Foto = models.FileField(upload_to='Images/%Y/%m/%d', blank=False)
    Dono = models.ForeignKey(User)
    DataRegistro = models.IntegerField(blank=True, null=True)
    Email = models.CharField(blank=True, null=True)
    Telefone = models.DateTimeField(null=True)


