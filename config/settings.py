from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv() 


STATIC_URL = '/static/'
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY='django-insecure-*v-phx*4a3z1$zb63stqr!*9!s@7sodevwirup7*nqtpb$g96t'
DEBUG= True
ALLOWED_HOSTS=['*'] 
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MODE = os.getenv("MODE")

BASE_DIR = Path(__file__).resolve().parent.parent

APPEND_SLASH=False
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "drf_spectacular",
    "corsheaders",
    "rest_framework",
    "core.fabricaNeeds",
    'core.usuario',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("core.usuario.authentication.TokenAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticatedOrReadOnly",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "PAGE_SIZE": 10,
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

if MODE in ["PRODUCTION", "MIGRATE"]:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('PGDATABASE'),
            'USER': os.getenv('PGUSER'),
            'PASSWORD': os.getenv('PGPASSWORD'),
            'HOST': os.getenv('PGHOST'),
            'PORT': os.getenv('PGPORT', 5432),
        'OPTIONS': {
         'sslmode': 'require',
    },
  }
}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }




LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True

SPECTACULAR_SETTINGS = {
    "TITLE": "FabricaNeeds API",
    "DESCRIPTION": "API para gerenciamento de estoque e demandas da Fabrica de Software",
    "VERSION": "1.0.0",
}

AUTH_USER_MODEL = "usuario.Usuario"


PASSAGE_APP_ID = '2TXjjhFWhntb7WqVkG46xAmb'
PASSAGE_API_KEY = 'WG7v8fQtFx.eQpT8x7cBDY3NITVXUGLgEDWSg4eNUGDKzlFIRBfg7P7fUROLPpkgANHLGhCYesq'
PASSAGE_AUTH_STRATEGY = 2