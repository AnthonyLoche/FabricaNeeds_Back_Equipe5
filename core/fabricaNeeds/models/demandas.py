from django.db import models
from .estoque import Estoque

class Demandas(models.Model):
    produto = models.OneToOneField(Estoque, on_delete=models.CASCADE, null=True)
    produto_nao_cadastrado = models.CharField(max_length=100, null=True)
    quantidade = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto.item} (ID: {self.produto.id}) - {self.data} - Quantidade: {self.quantidade}"
    
    class Meta:
        verbose_name = "Demanda"
        verbose_name_plural = "Demandas"
