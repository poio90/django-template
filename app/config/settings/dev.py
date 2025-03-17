import os

from .base import *

SECRET_KEY = os.getenv("SECRET_KEY","django-insecure-ony7(@81^+^2+75*aujva1)##1brz9_&)7(9_@v65yttry*3ow")
DEBUG = os.getenv("DEBUG", True)

ALLOWED_HOSTS = ["*"]

THIRD_PARTY_APP = [
    "django_extensions",
]  # third party apps goes here

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APP

# If you want to use postgresql instead, then uncomment this and comment that of sqlite3 bellow.
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": os.getenv("DB_NAME"),
#         "USER": os.getenv("DB_USER"),
#         "PASSWORD": os.getenv("DB_PWD"),
#         "HOST": os.getenv("DB_HOST"),
#         "PORT": os.getenv("DB_PORT"),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}