from django.db import models
from django.contrib.auth.models import User
from AdoteNaoCompreSITE.models.state import State


class User_extras(models.Model):
    Id = models.AutoField(primary_key=True)
    IdPai = models.ForeignKey(User)
    IdEstado = models.ForeignKey(State, default='1')
    Cidade = models.CharField(max_length=25)
    Telefone = models.PositiveIntegerField(blank=True, null=True)
    Celular = models.PositiveIntegerField(blank=True, null=True)
    CEP = models.PositiveIntegerField(blank=True, null=True)
    Tentativas = models.PositiveIntegerField(blank=False, null=False, default=0)


