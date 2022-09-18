from django.db import models

# Create your models here.
class Questao(models.Model):
    descricao = models.CharField(max_length=200,null=True)
    alternativa1 = models.CharField(max_length=200,null=True)
    alternativa2 = models.CharField(max_length=200,null=True)
    alternativa3 = models.CharField(max_length=200,null=True)
    alternativa4 = models.CharField(max_length=200,null=True)
    resposta = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.descricao