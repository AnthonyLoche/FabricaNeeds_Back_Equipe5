# Generated by Django 4.2.13 on 2024-08-22 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fabricaNeeds', '0002_pagamentos_alter_demandas_produto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandas',
            name='nome_produto',
        ),
        migrations.AlterField(
            model_name='demandas',
            name='produto',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='fabricaNeeds.estoque'),
        ),
    ]
