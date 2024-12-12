from django.db import models

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
