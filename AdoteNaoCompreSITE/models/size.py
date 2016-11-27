from django.db import models


class Size(models.Model):

    Id = models.AutoField(primary_key=True)
    Info = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.Info
