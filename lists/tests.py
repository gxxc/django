from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

class test(TestCase):
    def test_resolve_url(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)
