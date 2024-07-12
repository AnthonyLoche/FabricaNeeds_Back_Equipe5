from django.db import models
from localflavor.br.models import BRCPFField


class Pagamentos(models.Model):
    payment_id = models.AutoField(primary_key=True, null=False)
    cliente = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    cpf = BRCPFField(max_length=11, null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.BooleanField(null=False)
    
    def __str__(self):
        return f"{self.cliente} - {self.valor} - {self.status} - {self.email} - {self.cpf}"
    
    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"
    