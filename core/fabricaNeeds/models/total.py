from django.db import models

class Total(models.Model):
    total = models.IntegerField()

    def __str__(self):
        return f"Total: {self.total}"
    
    class Meta:
        verbose_name = "Total"