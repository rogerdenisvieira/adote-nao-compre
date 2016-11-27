from django.contrib.auth.models import User
from django.db import models

from AdoteNaoCompreSITE.models.breed import Breed
from AdoteNaoCompreSITE.models.size import Size
from AdoteNaoCompreSITE.models.behavior import Behavior


class Dog(models.Model):
    SEX_CHOICES = (('M', 'Macho'), ('F', 'Femea'))

    Id = models.AutoField(primary_key=True)
    IdProtetor = models.ForeignKey(User)
    IdRaca = models.ForeignKey(Breed, default='1')
    IdTamanho = models.ForeignKey(Size, default='1')
    IdComportamento = models.ForeignKey(Behavior, default='1')
    Nome = models.CharField(max_length=20, blank=False)
    Info = models.CharField(max_length=100, blank=False)
    Foto = models.FileField(upload_to='Images/%Y/%m/%d', blank=False)
    Interesse = models.BooleanField(default=False)
    Idade = models.IntegerField(blank=True, null=True)
    Peso = models.FloatField(blank=False, null=True)
    Sexo = models.CharField(max_length=2, choices=SEX_CHOICES, default='M', blank=False)
    DataRegistro = models.DateTimeField(null=True)
