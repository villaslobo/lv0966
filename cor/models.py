from django.db import models


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    def __str__(self):
        return "%s" % (self.nome)