import os
from pathlib import Path

import dj_database_url


# ==========================================================
# BASE DIRECTORY
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================================
# SECURITY
# ==========================================================

# Local fallback key.
# On Render, we will add a secure SECRET_KEY as an
# environment variable.
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-local-development-key-change-on-render"
)


# Local computer = True
# Render production = False
DEBUG = "RENDER" not in os.environ


# Hosts allowed during local development
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# Render automatically provides this hostname
RENDER_EXTERNAL_HOSTNAME = os.environ.get(
    "RENDER_EXTERNAL_HOSTNAME"
)

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(
        RENDER_EXTERNAL_HOSTNAME
    )


# Optional custom domain for later
CUSTOM_DOMAIN = os.environ.get(
    "CUSTOM_DOMAIN"
)

if CUSTOM_DOMAIN:
    ALLOWED_HOSTS.append(
        CUSTOM_DOMAIN
    )


# ==========================================================
# APPLICATIONS
# ==========================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # YOUR APPS
    "accounts",
    "courses",
    "website",
    "teachers",
]


# ==========================================================
# MIDDLEWARE
# ==========================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise serves static files in production
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==========================================================
# URL CONFIGURATION
# ==========================================================

ROOT_URLCONF = "core.urls"


# ==========================================================
# TEMPLATES
# ==========================================================

TEMPLATES = [
    {
        "BACKEND": (
            "django.template.backends.django."
            "DjangoTemplates"
        ),

        "DIRS": [],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                (
                    "django.template.context_processors."
                    "request"
                ),

                (
                    "django.contrib.auth."
                    "context_processors.auth"
                ),

                (
                    "django.contrib.messages."
                    "context_processors.messages"
                ),
            ],
        },
    },
]


# ==========================================================
# WSGI / ASGI
# ==========================================================

WSGI_APPLICATION = "core.wsgi.application"

ASGI_APPLICATION = "core.asgi.application"


# ==========================================================
# DATABASE
# ==========================================================

# On Render:
# Uses PostgreSQL when DATABASE_URL exists.
#
# On your computer:
# Uses your existing SQLite database.

DATABASE_URL = os.environ.get(
    "DATABASE_URL"
)


if DATABASE_URL:

    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }

else:

    DATABASES = {
        "default": {
            "ENGINE": (
                "django.db.backends.sqlite3"
            ),

            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# ==========================================================
# PASSWORD VALIDATION
# ==========================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth."
            "password_validation."
            "UserAttributeSimilarityValidator"
        )
    },

    {
        "NAME": (
            "django.contrib.auth."
            "password_validation."
            "MinimumLengthValidator"
        )
    },

    {
        "NAME": (
            "django.contrib.auth."
            "password_validation."
            "CommonPasswordValidator"
        )
    },

    {
        "NAME": (
            "django.contrib.auth."
            "password_validation."
            "NumericPasswordValidator"
        )
    },
]


# ==========================================================
# INTERNATIONALIZATION
# ==========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# ==========================================================
# STATIC FILES
# ==========================================================

STATIC_URL = "/static/"


# IMPORTANT:
# Your static files are already inside your Django apps,
# for example:
#
# website/static/website/
#
# Therefore, STATICFILES_DIRS is NOT needed.

STATIC_ROOT = BASE_DIR / "staticfiles"


# WhiteNoise production static file storage
STORAGES = {
    "default": {
        "BACKEND": (
            "django.core.files.storage."
            "FileSystemStorage"
        ),
    },

    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage."
            "CompressedManifestStaticFilesStorage"
        ),
    },
}


# ==========================================================
# LOGIN / LOGOUT
# ==========================================================

LOGIN_URL = "/login/"

LOGIN_REDIRECT_URL = "/dashboard/"

LOGOUT_REDIRECT_URL = "/"


# ==========================================================
# PRODUCTION SECURITY
# ==========================================================

if not DEBUG:

    # Render handles HTTPS through its proxy
    SECURE_PROXY_SSL_HEADER = (
        "HTTP_X_FORWARDED_PROTO",
        "https",
    )

    SECURE_SSL_REDIRECT = True

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True


    # Allow POST requests from your Render website
    if RENDER_EXTERNAL_HOSTNAME:

        CSRF_TRUSTED_ORIGINS = [
            "https://" + RENDER_EXTERNAL_HOSTNAME
        ]

    else:

        CSRF_TRUSTED_ORIGINS = []


# ==========================================================
# DEFAULT PRIMARY KEY
# ==========================================================

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)