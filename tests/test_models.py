# -*- coding: utf-8 -*-
import traceback

from django.core.exceptions import ValidationError
from django.test import TestCase

from des.models import DynamicEmailConfiguration


class DynamicEmailConfigurationTestCase(TestCase):

    def setUp(self):
        pass

    def test_use_ssl_and_use_tls_raises(self):
        configuration = DynamicEmailConfiguration()
        try:
            configuration.use_ssl = True
            configuration.use_tls = True
            configuration.clean()
            self.fail("No exception thrown. Expected ValidationError")
        except ValidationError:
            pass  # Test succeeded
        except Exception:
            self.fail("Incorrect exception thrown: {}".format(traceback.format_exc()))

    def test_use_tls_and_not_use_ssl_works(self):
        try:
            configuration = DynamicEmailConfiguration()
            configuration.use_ssl = False
            configuration.use_tls = True
            configuration.clean()
        except Exception:
            self.fail("Exception thrown:" + traceback.format_exc())

    def test_use_ssl_and_not_use_tls_works(self):
        try:
            configuration = DynamicEmailConfiguration()
            configuration.use_ssl = True
            configuration.use_tls = False
            configuration.clean()
        except Exception:
            self.fail("Exception thrown:" + traceback.format_exc())

    def test___str___works(self):
        configuration = DynamicEmailConfiguration()
        self.assertIsNotNone(configuration.__str__())
        self.assertNotEqual(configuration.__str__(), "")
