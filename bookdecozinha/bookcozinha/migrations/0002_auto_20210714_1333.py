# Generated by Django 3.2.5 on 2021-07-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcozinha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapio',
            name='informacoes_basicas',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='ingrediente',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='modo_de_preparo',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='nome_receita',
            field=models.TextField(max_length=100),
        ),
    ]
