from django.db import models


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True, max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9, unique=True)
    celular = models.CharField(max_length=14)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
