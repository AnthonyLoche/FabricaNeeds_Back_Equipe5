from django.db import models

class Retiradas(models.Model):
    retirada = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f" {self.data}"

    class Meta:
        verbose_name = "Retirada"
        verbose_name_plural = "Retiradas"
