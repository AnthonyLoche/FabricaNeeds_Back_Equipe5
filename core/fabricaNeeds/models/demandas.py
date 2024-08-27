from django.db import models
from .estoque import Estoque

class Demandas(models.Model):
    produto = models.CharField(max_length=100, null=False, blank=False)
    quantidade = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
     if self.produto is None:
        return f"Produto não definido - {self.data} - Quantidade: {self.quantidade}"
     return f"{self.produto} - {self.data} - Quantidade: {self.quantidade}"
    class Meta:
        verbose_name = "Demanda"
        verbose_name_plural = "Demandas"
