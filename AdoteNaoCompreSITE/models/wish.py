from django.db import models
from django.contrib.auth.models import User
from AdoteNaoCompreSITE.models.dog import Dog

class Wish(models.Model):
    Id = models.AutoField(primary_key=True)
    IdCao = models.ForeignKey(Dog)
    IdProtetor = models.ForeignKey(User)
    IdInteressado = models.ForeignKey(User)
    DataRegistro = models.DateTimeField(blank=False, null=True)