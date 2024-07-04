from django.db import models
# from .contribuicoes import Contribuinte
from .estoque import Estoque

class RetirarEstoque(models.Model):
    # usuario = models.ForeignKey(Contribuinte, on_delete=models.CASCADE)
    produto = models.ForeignKey(Estoque, on_delete=models.CASCADE, default="")
    quantidade = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f" {self.data} - Produto: {self.produto.item} - Quantidade: {self.quantidade}"

    class Meta:
        verbose_name = "Retirada de Estoque"
        verbose_name_plural = "Retiradas de Estoque"