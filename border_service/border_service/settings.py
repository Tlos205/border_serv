from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-a@%hd0+$i!+#)#yv@y3+)i$-fc(xeb-ibgac))b1p&we@eo&e3'

DEBUG = True

if DEBUG:
    ALLOWED_HOSTS=[]
else:
    ALLOWED_HOSTS = ['karelia-border.ru', 'www.karelia-border.ru', '84.201.180.60']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    #------------------------#
    'mainapp',
    'ckeditor',
    'ckeditor_uploader',
    'meta',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'border_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'border_service.wsgi.application'

# Импортируем заранее — если пакета нет, упадём сразу при старте, а не в runtime
try:
    import dj_database_url
except ImportError:
    dj_database_url = None


# === DATABASES ===
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL and dj_database_url:
    DATABASES = {
        'default': dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=True if 'sslmode=require' in DATABASE_URL else False
        )
    }
else:
    # Только для локальной разработки
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
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

# ---- в проде работало с этими данными ---- #
# STATIC_ROOT = '/app/staticfiles'
# MEDIA_ROOT = '/app/media'


LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'          # или ваш SMTP
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'no-reply@yourdomain.ru'
EMAIL_HOST_PASSWORD = 'your_password'
DEFAULT_FROM_EMAIL = 'no-reply@yourdomain.ru'

# ReCaptcha v3 (если используешь)
RECAPTCHA_PUBLIC_KEY = 'твой_публичный_ключ'
RECAPTCHA_PRIVATE_KEY = 'твой_приватный_ключ'
RECAPTCHA_DEFAULT_SCORE = 0.5

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': '100%',
    },
}


# Базовый домен и протокол (можно использовать sites-фреймворк)
# META_SITE_DOMAIN = 'karelia-border.ru'  # Твой домен
META_SITE_DOMAIN = '127.0.0.1:8000'  # Твой домен
# META_SITE_PROTOCOL = 'https'     # Или 'http' для dev
META_SITE_PROTOCOL = 'http'     # Или 'http' для dev
META_USE_SITES = False           # True, если используешь django.contrib.sites

# Включаем/выключаем типы тегов
META_USE_OG_PROPERTIES = True    # OpenGraph (Facebook)
META_USE_TWITTER_PROPERTIES = True  # Twitter Cards
META_USE_SCHEMAORG_PROPERTIES = True  # Schema.org (JSON-LD)

# Базовый URL для изображений (аналог STATIC_URL)
META_IMAGE_URL = '/media/'  # Путь к изображениям в meta-тегах

# Ключевые слова по умолчанию (если не заданы в view)
META_USE_DEFAULT_KEYWORDS = True
META_INCLUDE_KEYWORDS = ['django', 'meta']  # Твои глобальные ключевые слова

# Другие опции (см. docs: https://django-meta.readthedocs.io/en/latest/settings.html)
META_USE_TITLE_IN_META = True  # Авто-генерация title в meta

CSRF_TRUSTED_ORIGINS = [
    'https://karelia-border.ru',
    'https://www.karelia-border.ru',
]