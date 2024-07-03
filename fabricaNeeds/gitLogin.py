# from django.shortcuts import redirect
# from dj_rest_auth.registration.views import SocialLoginView
# from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client

# class GitHubLogin(SocialLoginView):
#     adapter_class = GitHubOAuth2Adapter

#     def get_adapter(self, request):
#         adapter = self.adapter_class(request)
#         adapter.client_class = OAuth2Client
#         return adapter

#     def get(self, request, *args, **kwargs):
#         # Definindo a callback_url para o GitHubOAuth2Adapter, se necessário
#         adapter = self.get_adapter(request)
#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         # Definindo a callback_url para o GitHubOAuth2Adapter, se necessário
#         adapter = self.get_adapter(request)
#         response = super().post(request, *args, **kwargs)
        
#         # Verificando se há erros no response
#         if 'non_field_errors' in response.data:
#             return response
        
#         # Implemente lógica adicional conforme necessário para manipular a resposta

#         return response
