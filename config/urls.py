from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from fabricaNeeds.aimeucu import GitHubLogin

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.urls import path, include
from social_django import urls as social_django_urls
from rest_framework.routers import DefaultRouter
from fabricaNeeds.views import TotalViewSet, EstoqueViewSet, DemandasViewSet, RetirarEstoqueViewSet, EntradasEstoqueViewSet, ContribuinteViewSet, loginViewSet

router = DefaultRouter()
router.register(r"total", TotalViewSet)
router.register(r"stock", EstoqueViewSet)
router.register(r"demands", DemandasViewSet)
router.register(r"removeStock", RetirarEstoqueViewSet)
router.register(r"addStock", EntradasEstoqueViewSet)
router.register(r"clients", ContribuinteViewSet)

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
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/github/', include(social_django_urls, namespace='social')),
    path('dj-rest-auth/github/login/', GitHubLogin.as_view(), name='github_login'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
