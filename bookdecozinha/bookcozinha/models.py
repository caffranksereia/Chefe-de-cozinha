from django.db import models

# Create your models here.

class cardapio(models.Model):
    #fields
    nome_receita = models.TextField(max_length=100)
    ingrediente = models.TextField(max_length=2000)
    modo_de_preparo = models.TextField(max_length=2000)
    informacoes_basicas = models.TextField(max_length=2000)

