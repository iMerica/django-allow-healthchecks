from django.conf import settings
from django.core.exceptions import DisallowedHost
from django.test import override_settings, TestCase, RequestFactory
from django.utils.module_loading import import_string
from django_allow_healthchecks.middleware import ByPassForHealthChecks
from django.middleware.common import CommonMiddleware


class TestMiddleware(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.rf = RequestFactory()

    def test_raises_error(self):
        """ Verify existing invalid hosts raise an exception """
        with self.assertRaises(DisallowedHost):
            req = self.rf.get('/',  HTTP_HOST='192.168.1.17', REMOTE_ADDR='192.168.1.17')
            mw = CommonMiddleware()
            mw.process_request(req)

    @override_settings(ALLOWED_HOSTS=['example.com'], HEALTH_CHECK_HEADER_VALUE='XYZ-789')
    def test_bypass_with_allowed_header(self):
        """ Verify we can bypass exceptions """
        self.assertEqual(settings.ALLOWED_HOSTS, ['example.com'])
        headers = {
            'HTTP_X-Health': 'XYZ-789',
            'HTTP_HOST': 'invalid-host.com'
        }
        req = self.rf.get('/', **headers)
        self.assertIsNone(self.middleware(req))

    @override_settings(ALLOWED_HOSTS=['example.com'], HEALTH_CHECK_HEADER_VALUE='XYZ-789')
    def test_bypass_headers_invalid(self):
        """ Verify that when a host """
        self.assertEqual(settings.ALLOWED_HOSTS, ['example.com'])
        headers = {
            'HTTP_X-Health': 'xxxx',
            'HTTP_HOST': 'invalid-host.com'
        }
        with self.assertRaises(DisallowedHost):
            req = self.rf.get('/', **headers)
            self.middleware(req)
            for middleware in settings.BASE_MW:
                mw = import_string(middleware)()
                mw.process_request(req)

    @property
    def middleware(self):
        return ByPassForHealthChecks().process_request
