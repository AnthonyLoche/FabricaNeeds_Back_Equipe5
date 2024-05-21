# Generated by Django 5.0.4 on 2024-05-21 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabricaNeeds', '0021_demandas_nome_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandas',
            name='nome_produto',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='demandas',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fabricaNeeds.estoque', unique=True),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='item',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
