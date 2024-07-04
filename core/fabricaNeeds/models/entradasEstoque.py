from django.db import models
from .demandas import Demandas

class EntradasEstoque(models.Model):
    demanda = models.ForeignKey(Demandas, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.demanda.produto} - {self.data} - Quantidade: {self.quantidade}"
    
    class Meta:
        verbose_name = "Entrada de Estoque"
        verbose_name_plural = "Entradas de Estoque"