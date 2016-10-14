from django.db import models
from django.contrib.auth.models import User
from AdoteNaoCompreSITE.models.breed import Breed


class Dog(models.Model):
    SEX_CHOICES = (('M', 'Macho'), ('F', 'Femea'))

    Id = models.AutoField(primary_key=True)
    IdProtetor = models.ForeignKey(User)
    IdRaca = models.ForeignKey(Breed, default='1')
    Nome = models.CharField(max_length=20)
    Info = models.CharField(max_length=100)
    Foto = models.FileField(upload_to='Images/%Y/%m/%d')
    Interesse = models.BooleanField(default=False)
    Idade = models.IntegerField(blank=True, null=True)
    Sexo = models.CharField(max_length=2, choices=SEX_CHOICES, default='M')
    DataRegistro = models.DateTimeField(blank=False, null=True)
