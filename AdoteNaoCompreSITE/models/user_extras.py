from django.db import models
from django.contrib.auth.models import User


class User_extras(models.Model):
    Id = models.AutoField(primary_key=True)
    IdPai = models.ForeignKey(User)
    Estado = models.CharField(max_length=2)
    Cidade = models.CharField(max_length=25)
    Telefone = models.IntegerField(blank=True, null=True)
    Celular = models.IntegerField(blank=True, null=True)
    CEP = models.IntegerField(blank=True, null=True)
    Tentativas = models.IntegerField(blank=False, null=False, default=0)


