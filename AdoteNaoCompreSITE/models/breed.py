from django.db import models


class Breed(models.Model):
    Id = models.AutoField(primary_key=True)
    Info = models.CharField(max_length=100)

    def __str__(self):
        return self.Info
