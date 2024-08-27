# Generated by Django 4.2.13 on 2024-08-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabricaNeeds', '0006_alter_demandas_produto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandas',
            name='produto_nao_cadastrado',
        ),
        migrations.AlterField(
            model_name='demandas',
            name='produto',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EntradasEstoque',
        ),
    ]
