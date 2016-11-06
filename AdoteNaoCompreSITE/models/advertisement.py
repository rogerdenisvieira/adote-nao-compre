from django.contrib.auth.models import User
from django.db import models


class Advertisement(models.Model):
    Id = models.AutoField(primary_key=True)
    Descricao = models.CharField(max_length=100)
    Banner = models.FileField(upload_to='Images/%Y/%m/%d', blank=False)
    Dono = models.ForeignKey(User)
    DataRegistro = models.DateTimeField(null=True)
    Email = models.CharField(blank=True, null=True, max_length=100)
    Telefone = models.IntegerField(blank=True, null=True)
