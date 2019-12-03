from django.conf import settings

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class ByPassForHealthChecks(MiddlewareMixin):
    def process_request(self, request):
        host = self.get_host(request)
        health_check_header = request.headers.get('X-Health')
        if health_check_header == settings.HEALTH_CHECK_HEADER_VALUE:
            settings.ALLOWED_HOSTS += [host]
        return None

    @staticmethod
    def get_host(request):
        if settings.USE_X_FORWARDED_HOST and ('HTTP_X_FORWARDED_HOST' in request.META):
            host = request.META['HTTP_X_FORWARDED_HOST']
        elif 'HTTP_HOST' in request.META:
            host = request.META['HTTP_HOST']
        else:
            # Reconstruct the host using the algorithm from PEP 333.
            host = request.META['SERVER_NAME']
            server_port = request.get_port()
            if server_port != ('443' if request.is_secure() else '80'):
                host = '%s:%s' % (host, server_port)
        return host
