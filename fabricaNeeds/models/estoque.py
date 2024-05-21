from django.db import models

class Estoque(models.Model):
    item = models.CharField(max_length=100, unique=True)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f"Produto: {self.item} - Quantidade: {self.quantidade}"
    
    class Meta:
        verbose_name = "Estoque"