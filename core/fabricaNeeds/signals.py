from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Total, Retiradas

import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

@receiver(post_save, sender=Retiradas)
@receiver(post_delete, sender=Retiradas)
def atualizar_total_contribuicoes(sender, instance, **kwargs):
    total_obj, created = Total.objects.get_or_create(pk=1)
    
    if kwargs.get('created', True):  
        total_obj.total -= instance.retirada
    
    total_obj.save()

# @receiver(post_save, sender=EntradasEstoque)
# @receiver(post_delete, sender=EntradasEstoque)
# def atualizar_demandas(sender, instance, **kwargs):
#     demanda_obj, created = Demandas.objects.get_or_create(pk=instance.demanda.id)

#     if kwargs.get('created', True):
#         demanda_obj.quantidade -= instance.quantidade
#         print(demanda_obj.quantidade)
#     else:
#         demanda_obj.quantidade += instance.quantidade

#     demanda_obj.save()

# @receiver(post_save, sender=EntradasEstoque)
# @receiver(post_delete, sender=EntradasEstoque)
# def atualizar_estoque(sender, instance, **kwargs):
#     atualizar_obj, _ = Estoque.objects.get_or_create(pk=instance.demanda.produto.id)
    
#     if kwargs.get('created', True):
#         atualizar_obj.quantidade += instance.quantidade
#     else:
#         atualizar_obj.quantidade -= instance.quantidade
    
#     atualizar_obj.save()


