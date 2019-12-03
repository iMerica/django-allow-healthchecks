# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django

DEBUG = False
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "#d$q79db1elfa9-6#-%4x!7*n8@vp@b*$c9nj#uti!(r5*(-@9"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites"
]

ALLOWED_HOSTS = ['example.com']

SITE_ID = 1

BASE_MW = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if django.VERSION >= (1, 10):
    MIDDLEWARE = BASE_MW
else:
    MIDDLEWARE_CLASSES = BASE_MW

HEALTH_CHECK_HEADER_VALUE = 'XYZ-123'
