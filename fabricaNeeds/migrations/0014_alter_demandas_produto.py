# Generated by Django 5.0.4 on 2024-04-23 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabricaNeeds', '0013_alter_demandas_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandas',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fabricaNeeds.estoque'),
        ),
    ]
