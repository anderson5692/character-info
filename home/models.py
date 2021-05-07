from django.db import models

# Create your models here.
class Personagem(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)