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
            git_id = psg.getUser(psg_user_id)
            github_provider_id = git_id.social_connections.github.provider_id
            print(github_provider_id)
            user = self._get_user(github_provider_id)
        except AuthenticationFailed:
            raise
        except Exception as e:
            raise AuthenticationFailed(str(e)) from e

        return (user, None)

    def _get_user(self, github_provider_id):
        try:
            user = User.objects.get(github_id=github_provider_id)
            return user
        except ObjectDoesNotExist:
            return False

    def _get_user_id(self, request):
        try:
            return psg.authenticateRequest(request)
        except PassageError as e:
            raise AuthenticationFailed(str(e)) from e

    def _update_user_info(self, user, user_info):
        updated = False
        #exemplo
        if user.email != user_info["email"]:
            user.email = user_info["email"]
            updated = True

        if updated:
            user.save()
