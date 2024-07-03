# from django.db import models
# from django.contrib.auth.hashers import make_password, check_password

# class Contribuinte(models.Model):
#     nome = models.CharField(max_length=100, null=False, unique=True)
#     email = models.EmailField(null=False)
#     senha = models.CharField(max_length=100, null=False, default="1234")
#     token = models.CharField(max_length=10, null=True, default="")
#     verificado = models.BooleanField(default=False)

#     def __str__(self):
#         return self.nome
    
#     def save(self, *args, **kwargs):
#         # Verifica se a senha não está em formato hash
#         if not self.senha.startswith('pbkdf2_sha256'):
#             # Se não estiver em formato hash, faz o hash da senha
#             self.senha = make_password(self.senha)
#         super().save(*args, **kwargs)
    
#     class Meta:
#         verbose_name = "Contribuinte"
#         verbose_name_plural = "Contribuintes"
