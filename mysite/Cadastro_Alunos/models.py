from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField(3)
    grupo = models.CharField(max_length=30)
    academia = models.CharField(max_length=30)

    def getName(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getGrupo(self):
        return self.grupo
    def getAcademia(self):
        return self.academia
        



