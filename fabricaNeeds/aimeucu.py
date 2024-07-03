from django.shortcuts import redirect # type: ignore
from allauth.socialaccount.models import SocialToken # type: ignore
from dj_rest_auth.registration.views import SocialLoginView # type: ignore
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter # type: ignore

class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = SocialToken.objects.get(account__user=request.user, account__provider='github')  # Corrigindo o acesso aos objetos relacionados
        response.data['token'] = str(token)
        return response
