from django.shortcuts import redirect
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter

class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter

    def get(self, request, *args, **kwargs):
        # Definindo a callback_url para o GitHubOAuth2Adapter
        self.adapter_class.callback_url = 'http://localhost:8000/dj-rest-auth/github/login/'
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Definindo a callback_url para o GitHubOAuth2Adapter
        self.adapter_class.callback_url = 'http://localhost:8000/dj-rest-auth/github/login/'
        self.adapter_class = GitHubOAuth2Adapter(request)
        self.adapter_class.complete_login(request)
        return redirect('/')
