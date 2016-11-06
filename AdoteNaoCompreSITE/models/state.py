from django.db import models


class State(models.Model):
    Id = models.AutoField(primary_key=True)
    Descricao = models.CharField(max_length=100, blank=False)
    Sigla = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.Descricao
