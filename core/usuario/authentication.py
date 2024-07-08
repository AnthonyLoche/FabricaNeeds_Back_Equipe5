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
            user, created = self._get_or_create_user(psg_user_id)
            user_info = self._verify_github_organization_membership(user)
            self._update_user_info(user, user_info)
        except AuthenticationFailed:
            raise
        except Exception as e:
            raise AuthenticationFailed(str(e)) from e

        return (user, user_info)

    def _get_or_create_user(self, psg_user_id):
        try:
            user = User.objects.get(passage_id=psg_user_id)
            created = False
        except ObjectDoesNotExist:
            try:
                psg_user = psg.getUser(psg_user_id)
                user = User.objects.create_user(
                    passage_id=psg_user.id,
                    email=psg_user.email,
                    github_token=psg_user.identities[0].oauth.access_token
                )
                created = True
            except PassageError as e:
                raise AuthenticationFailed(str(e)) from e

        return user, created

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
        response.raise_for_status() 

        user_data = response.json()
        username = user_data.get("login")
        email = user_data.get("email")
        avatar_url = user_data.get("avatar_url")

        org_response = requests.get(f"{GITHUB_API_URL}/orgs/{GITHUB_ORG}/members/{username}", headers=headers)
        is_in_organization = org_response.status_code == 204

        return {
            "is_in_organization": is_in_organization,
            "github_username": username,
            "email": email,
            "avatar_url": avatar_url
        }

    def _update_user_info(self, user, user_info):
        updated = False

        if user.github_username != user_info["github_username"]:
            user.github_username = user_info["github_username"]
            updated = True

        if user.picture != user_info["avatar_url"]:
            user.picture = user_info["avatar_url"]
            updated = True

        if user.verified != user_info["is_in_organization"]:
           
            user.verified = user_info["is_in_organization"]
            updated = True

        if updated:
            user.save()
