from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = []


# Application definition

DEFAULT_APP = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CREATED_APP = [
    "apps.core.apps.CoreConfig",
]  # custom apps goes here

THIRD_PARTY_APP = []  # third party apps goes here

INSTALLED_APPS = [*DEFAULT_APP, *CREATED_APP, *THIRD_PARTY_APP]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGES = [
    # ("ar", _("Arabic")),
    # ("az", _("Azerbaijani")),
    # ("bg", _("Bulgarian")),
    # ("ca", _("Catalan")),
    # ("cs", _("Czech")),
    # ("da", _("Danish")),
    # ("de", _("German")),  #
    # ("el", _("Greek")),
    ("en", _("English")),  #
    ("es", _("Spanish")),  #
    # ("et", _("Estonian")),
    # ("eu", _("Basque")),
    # ("fa", _("Persian")),
    # ("fi", _("Finnish")),
    # ("fr", _("French")),  #
    # ("he", _("Hebrew")),
    # ("hr", _("Croatian")),
    # ("hu", _("Hungarian")),
    # ("id", _("Indonesian")),
    # ("it", _("Italian")),  #
    # ("ja", _("Japanese")),  #
    # ("ka", _("Georgian")),
    # ("ko", _("Korean")),  #
    # ("ky", _("Kyrgyz")),
    # ("lt", _("Lithuanian")),
    # ("lv", _("Latvian")),
    # ("mn", _("Mongolian")),
    # ("nb", _("Norwegian Bokmål")),
    # ("nl", _("Dutch")),
    # ("pl", _("Polish")),
    # ("pt-BR", _("Portuguese (Brazil)")),  #
    # ("pt-PT", _("Portuguese (Portugal)")),
    # ("ro", _("Romanian")),
    # ("ru", _("Russian")),
    # ("sk", _("Slovak")),
    # ("sl", _("Slovenian")),
    # ("sr", _("Serbian")),
    # ("sr-Latn", _("Serbian (Latin)")),
    # ("sv", _("Swedish")),
    # ("th", _("Thai")),
    # ("tr", _("Turkish")),
    # ("uk", _("Ukrainian")),
    # ("zh-hans", _("Chinese (Simplified)")),  #
    # ("zh-hant", _("Chinese (Traditional)")),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]
