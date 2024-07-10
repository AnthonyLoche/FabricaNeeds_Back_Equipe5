import requests
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from passageidentity import Passage, PassageError
from core.usuario.models import Usuario as User

PASSAGE_APP_ID = settings.PASSAGE_APP_ID
PASSAGE_API_KEY = settings.PASSAGE_API_KEY
PASSAGE_AUTH_STRATEGY = settings.PASSAGE_AUTH_STRATEGY


psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY, auth_strategy=PASSAGE_AUTH_STRATEGY)


class TokenAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = 'core.authentication.TokenAuthentication'
    name = 'tokenAuth'
    match_subclasses = True
    priority = -1

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name='Authorization',
            token_prefix='Bearer',
        )


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        if not request.headers.get("Authorization"):
            return None

        try:
            psg_user_id = self._get_user_id(request)
            user = self._get_or_create_user(psg_user_id)
            user.passage_id = psg.getUser(psg_user_id).passage_id
        except AuthenticationFailed:
            raise
        except Exception as e:
            raise AuthenticationFailed(str(e)) from e

        return (user, None)

    def _get_or_create_user(self, psg_user_id):
        try:
            user = User.objects.get(passage_id=psg_user_id)
        except ObjectDoesNotExist:
            try:
                psg_user = psg.getUser(psg_user_id)
                github_id = psg_user.social_connections.github.provider_id
                user_info = self._get_user_info(github_id)
                
                if not user_info:
                    raise AuthenticationFailed("Usuário não encontrado na organização GitHub")
                
                user = User.objects.create_user(
                    passage_id=psg_user.id,
                    email=psg_user.email,
                    github_id=github_id,
                    picture=user_info["picture"],
                    username=user_info["username"],
                )
            except PassageError as e:
                raise AuthenticationFailed(str(e)) from e

        return user

    def _get_user_id(self, request):
        try:
            return psg.authenticateRequest(request)
        except PassageError as e:
            raise AuthenticationFailed(str(e)) from e

    def _get_user_info(self, github_id):
        print("Entrou na função _get_user_info com o GitHub ID:", github_id)
        try:
            response = requests.get("https://api.github.com/orgs/fabricadesoftware-ifc/members")
            response.raise_for_status()
            print("Resposta da API GitHub recebida")

            for user in response.json():
                print("Processando usuário:", user['id'], github_id)
                if str(user["id"]) == str(github_id):
                    print("Usuário encontrado:", user)
                    return {
                        "username": user["login"],
                        "picture": user["avatar_url"]
                    }

            print("Usuário não encontrado na organização")
            return None

        except requests.RequestException as e:
            raise PassageError(f"Erro na requisição à API do GitHub: {str(e)}")
