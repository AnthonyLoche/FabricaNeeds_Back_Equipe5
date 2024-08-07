from django.db import models
# from .contribuicoes import Contribuinte
# from core.usuario.models import Usuario
class Retiradas(models.Model):
    # retirante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    retirada = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f" {self.data}"

    class Meta:
        verbose_name = "Retirada"
        verbose_name_plural = "Retiradas"
