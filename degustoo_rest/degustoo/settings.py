"""
Django settings for degustoo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!_b0og3m$m_u@tdbis#4n6l8_*)8hpaj0hhkjz2e-oria13lq('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

DEGUSTOO_APPS = (
    'degAuth',
    'core',
    'index',
    'administracao',
    'cliente',
    'restaurante',
)

THIRD_PART_APPS = (
    'rest_framework',
    'compressor',
    # 'hamlpy',
    # 'djaml',
)

INSTALLED_APPS = INSTALLED_APPS + DEGUSTOO_APPS + THIRD_PART_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'degustoo.urls'

WSGI_APPLICATION = 'degustoo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Auth
AUTH_USER_MODEL = 'degAuth.Usuario'     # custom user
LOGIN_URL = 'index:login'               # custom login

# E-Mail
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'Nome <email@gmail.com>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'email@gmail'
EMAIL_HOST_PASSWORD = 'pass'
EMAIL_PORT = 587

CONTACT_EMAIL = 'wallacycleyton@gmail.com'

#REST
REST_FRAMEWORK = {
    # 'DEFAULT_RENDERER_CLASSES':(
    #     'rest_framework.renderers.JSONRenderer',
    # )
}

#COMPRESSOR
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'compressor'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    #'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_ROOT = os.path.join(BASE_DIR, 'compressor')

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'sass --scss --compass {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/coffeescript', 'coffee -c --stdio'),
)

COMPRESS_URL = STATIC_URL

#TEMPLATE
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'hamlpy.template.loaders.HamlPyFilesystemLoader',
    'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
    'djaml.loaders.DjamlFilesystemLoader',
    'djaml.loaders.DjamlAppDirectoriesLoader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# TEMPLATE_LOADERS = (
#     ('django.template.loaders.cached.Loader', (
#         'djaml.loaders.DjamlAppDirectoriesLoader',
#         'djaml.loaders.DjamlFilesystemLoader',
#         'django.template.loaders.filesystem.Loader',
#         'django.template.loaders.app_directories.Loader',
#   )),
# )