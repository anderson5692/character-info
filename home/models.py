from django.db import models

# Create your models here.
class Personagem(models.Model):
    Nome = models.CharField(max_length=255)
    Idade = models.IntegerField(blank=True, null=True)
    Espécie = models.CharField(max_length=255)
    Gênero = models.CharField(max_length=255)
    Ocupação = models.CharField(max_length=255)
    Descrição = models.TextField(max_length=255)

    def __str__(self):
        return self.Nome

