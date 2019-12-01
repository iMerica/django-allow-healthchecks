from django.conf import settings

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class ByPassForHealthChecks(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        host = request.get_host()
        health_check_header = request.headers.get('X-Health')
        if health_check_header == settings.HEALTH_CHECK_HEADER_VALUE:
            settings.ALLOWED_HOSTS += [host]
        return None

