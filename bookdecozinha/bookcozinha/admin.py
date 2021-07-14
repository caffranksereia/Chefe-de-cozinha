from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import cardapio


class list_receita(admin.ModelAdmin):
    list_display = ['nome_receita', 'ingrediente', 'modo_de_preparo' ,'informacoes_basicas']
    search_receita = ['key']
    list_per_page = 10


admin.site.register(cardapio,list_receita)


