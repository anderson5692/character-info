from django.db import models

# Create your models here.
class Personagem(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerChoices(max_lenght=9999)
    especie = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    ocupacao = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)

    def __str__(self):
        return self.nome

