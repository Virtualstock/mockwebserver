# -*- coding: utf-8 -*-

from mockwebserver import MockWebServer
from mockwebserver.mockwebserver import Page
from unittest import TestCase


class TestServer(TestCase):
    def setUp(self):
        self.server = MockWebServer()

    def get(self, url):
        import requests
        return requests.get(self.server.url + url)

    def post(self, url, body):
        import requests
        return requests.post(self.server.url + url, body)

    def test_get_page(self):
        self.server.set('/page', 'content')
        with self.server:
            response = self.get('page')
            self.failUnless(response.ok)
            self.assertEqual('content', response.content)

    def test_post_page(self):
        page = self.server.set('/page', '')
        with self.server:
            response = self.post('page', 'content')
            self.failUnless(response.ok)
            self.assertEqual('content', page.request(1).body)

    def test_post_page_unicode_content(self):
        page = self.server.set('/page', '')
        page.set_content(u'', u'application/json')
        with self.server:
            response = self.post('page', u'@©')
            self.failUnless(response.ok)
            self.assertEqual('@©', page.request(1).body)


class TestPage(TestCase):
    def test_url_set_on_constructor(self):
        url = '/endpoint-url'
        page = Page('/endpoint-url')

        self.assertEqual(url, page.url)

    def test_set_content_unicode_string_returns_string(self):
        page = Page('/endpoint-url')
        page.set_content(u'@©', u'application/json')

        self.assertEqual(u'application/json', page.content_type)
        self.assertEqual('@©', page.content)

    def test_set_content_string_returns_string(self):
        page = Page('/endpoint-url')
        page.set_content('@©', 'application/json')

        self.assertEqual('application/json', page.content_type)
        self.assertEqual('@©', page.content)
