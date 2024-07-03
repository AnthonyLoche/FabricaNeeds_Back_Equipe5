from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv() 

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
STATIC_URL = '/static/'
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY='django-insecure-*v-phx*4a3z1$zb63stqr!*9!s@7sodevwirup7*nqtpb$g96t'
DEBUG= os.getenv("DEBUG", False)
ALLOWED_HOSTS=['*'] 
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MODE = os.getenv("MODE")

BASE_DIR = Path(__file__).resolve().parent.parent

SITE_ID = 1

APPEND_SLASH=False
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",
    "rest_framework",
    "fabricaNeeds",
    "drf_spectacular",
    'rest_framework.authtoken',
    'dj_rest_auth',
    'social_django',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github'   
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
    'corsheaders.middleware.CorsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
     'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
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


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Django's default auth backend
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]


SOCIAL_AUTH_GITHUB_KEY = 'Ov23lizI5bHOzJJEPBK1'
SOCIAL_AUTH_GITHUB_SECRET = 'ad66a279853a58ad13ce9508a0926ccb7f3a0f66'

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

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': ['user:email'],  
        'VERIFIED_EMAIL': True,
        'APP': {
            'client_id': SOCIAL_AUTH_GITHUB_KEY,
            'secret': SOCIAL_AUTH_GITHUB_SECRET,
        }
    }
}
