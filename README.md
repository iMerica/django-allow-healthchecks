
# Django Allow Health-checks


### Quickstart

Install django-allow-healthchecks

    pip3 install django-allow-healthchecks

Add the class to your middleware, ideally first in the list

```python

MIDDLEWARE = [
    'django_allow_healthchecks.middleware.ByPassForHealthChecks', # <~ Add this 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```

Assign your magical header value

    HEALTH_CHECK_HEADER_VALUE = 'XYZ-Health'
``
