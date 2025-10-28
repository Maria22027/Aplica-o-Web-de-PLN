"""
Django settings for core project.
Adaptado para o projeto de chat com MongoDB e interface simples.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# --- Caminho base do projeto ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Carrega variáveis de ambiente do arquivo .env ---
load_dotenv()

# --- Segurança ---
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-secret-key")  # Evita expor a key no código
DEBUG = True
ALLOWED_HOSTS = []

# --- Aplicações instaladas ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'interface',  # nome do teu app
]

# --- Middlewares padrão ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- Configuração das rotas principais ---
ROOT_URLCONF = 'core.urls'

# --- Configuração dos templates HTML ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Pasta onde estão os HTMLs do app
        'DIRS': [BASE_DIR / 'interface' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- Aplicação WSGI ---
WSGI_APPLICATION = 'core.wsgi.application'

# --- Banco SQLite padrão (usado só pro Django, não pro chat) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Validação de senhas padrão do Django ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Internacionalização ---
LANGUAGE_CODE = 'pt-br'  # muda pra português do Brasil
TIME_ZONE = 'America/Sao_Paulo'  # horário do Brasil
USE_I18N = True
USE_TZ = True

# --- Arquivos estáticos (CSS, JS, imagens) ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'interface' / 'static']

# --- ID padrão para novas tabelas Django ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Configurações do MongoDB ---
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")  # conexão local por padrão
MONGODB_DB = os.getenv("MONGODB_DB", "chat_db")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "interactions")
