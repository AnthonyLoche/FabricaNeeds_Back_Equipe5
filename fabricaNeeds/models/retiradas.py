from django.db import models
from .contribuicoes import Contribuinte

class Retiradas(models.Model):
    retirante = models.ForeignKey(Contribuinte, on_delete=models.CASCADE)
    retirada = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.retirante.nome} - {self.data}"

    class Meta:
        verbose_name = "Retirada"
        verbose_name_plural = "Retiradas"
