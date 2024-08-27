from django.contrib import admin
from .models import Total, Retiradas, Estoque,Demandas, Pagamentos

admin.site.register(Total)
admin.site.register(Retiradas)
admin.site.register(Estoque)
admin.site.register(Demandas)
# admin.site.register(EntradasEstoque)
admin.site.register(Pagamentos)