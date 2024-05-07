from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework.routers import DefaultRouter
from fabricaNeeds.views import TotalViewSet, EstoqueViewSet, DemandasViewSet, RetiradasViewSet, RetirarEstoqueViewSet, EntradasEstoqueViewSet, ContribuinteViewSet, ContribuicoesViewSet, loginViewSet

router = DefaultRouter()
router.register(r"total", TotalViewSet)
router.register(r"estoque", EstoqueViewSet)
router.register(r"demandas", DemandasViewSet)
router.register(r"retiradas", RetiradasViewSet)
router.register(r"retirarEstoque", RetirarEstoqueViewSet)
router.register(r"entradasEstoque", EntradasEstoqueViewSet)
router.register(r"contribuinte", ContribuinteViewSet)
router.register(r"contribuicoes", ContribuicoesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', loginViewSet.as_view(), name='login'),
    path("", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]



