# Generated by Django 3.2.5 on 2021-07-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cardapio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.TextField(max_length=200)),
                ('ingrediente', models.TextField(max_length=500)),
                ('modo_de_preparo', models.TextField(max_length=500)),
                ('informacoes_basicas', models.TextField(max_length=500)),
            ],
        ),
    ]