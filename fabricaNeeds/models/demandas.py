from django.db import models
from .estoque import Estoque

class Demandas(models.Model):
    produto = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    nome_produto = models.CharField(max_length=100, null=True) 
    quantidade = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.nome_produto = self.produto.item
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto.item} (ID: {self.produto.id}) - {self.data} - Quantidade: {self.quantidade}"
    
    class Meta:
        verbose_name = "Demanda"
        verbose_name_plural = "Demandas"
