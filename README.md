
# Django Allow Health-Checks


### Background

Kubernetes, loadbalancers and other PaaS have a concept of a health check. These are simple GET requests against an endpoint that you define which tells the orchestrator if a web worker is healthy or not. The problem is that these requests come from within the same network running your app using an non-deterministic hostname or IP address. So instead of making your allowed hosts wide open with `['*']` (to allow any requests to get by), you can simply install this package to allow these requests to occur without introducing more technical/security risks then neccessary.

For example, given a kubernetes deployment with the following details:

```yaml
#... other details
      containers:
      - name: app
        image: registry.gitlab.com/username/cool-app/app
        livenessProbe:
          httpGet:
            path: /health-check/
            port: 8000
            httpHeaders:
            - name: X-Health
              value:  XYZ-123
          initialDelaySeconds: 3
          periodSeconds: 60
        imagePullPolicy: Always
```
You can allow these requests to get by by simply adding this to your settings

    HEALTH_CHECK_HEADER_VALUE = 'XYZ-123'


### Setup

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


## Notes

Django 2.2+ only!
