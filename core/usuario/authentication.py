import os
import requests
from dotenv import load_dotenv
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from passageidentity import Passage, PassageError
from passageidentity.openapi_client.models import UserInfo
from core.usuario.models import Usuario as User

load_dotenv()

GITHUB_API = os.getenv("GITHUB_API")
PASSAGE_APP_ID = settings.PASSAGE_APP_ID
PASSAGE_API_KEY = settings.PASSAGE_API_KEY
PASSAGE_AUTH_STRATEGY = settings.PASSAGE_AUTH_STRATEGY
GITHUB_API_URL = "https://api.github.com"
GITHUB_ORG = "fabricadesoftware-ifc"

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
            self._verify_github_organization_membership(user)
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
                user = User.objects.create_user(
                    passage_id=psg_user.id,
                    email=psg_user.email,
                    github_token=psg_user.identities[0].oauth.access_token
                )
            except PassageError as e:
                raise AuthenticationFailed(str(e)) from e

        return user

    def _get_user_id(self, request):
        try:
            return psg.authenticateRequest(request)
        except PassageError as e:
            raise AuthenticationFailed(str(e)) from e

    def _verify_github_organization_membership(self, user):
        headers = {
            "Authorization": f"Bearer {GITHUB_API}",
            "Accept": "application/vnd.github.v3+json"
        }

        response = requests.get(f"{GITHUB_API_URL}/user", headers=headers)
        response.raise_for_status()  # Raise exception for non-200 status

        user_data = response.json()
        username = user_data.get("login")

        org_response = requests.get(f"{GITHUB_API_URL}/orgs/{GITHUB_ORG}/members/{username}", headers=headers)
        if org_response.status_code != 204:
            raise AuthenticationFailed("User is not a member of the organization")
