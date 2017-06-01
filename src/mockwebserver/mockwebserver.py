from threading import Thread
import attr


@attr.s
class Request(object):
    method = attr.ib()
    query = attr.ib()
    headers = attr.ib()
    body = attr.ib(default=None)


class MockWebServer(object):
    def __init__(self, host='', port=None):
        import random
        import BaseHTTPServer
        self._host = host or 'localhost'
        self._port = port or random.randint(20000, 50000)
        self._url = 'http://{0}:{1}/'.format(self._host, self._port)

        class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
            def handle_one_request(self, server=self):
                self.raw_requestline = self.rfile.readline(65537)
                if not self.parse_request():
                    # Either returns true or sends error response
                    return
                path, query = self.path, None
                if '?' in path:
                    path, query = path.split('?', 1)
                page = server._pages.get(path)
                if not page:
                    return self.send_error(404)
                body = self.rfile.read(int(self.headers.getheader('Content-Length', 0)))
                page._record_request(Request(
                        method=self.command,
                        query=query,
                        headers=self.headers,
                        body=body,
                        ))
                self.send_response(page.status, page.status_message)
                content = page.content
                if content:
                    self.send_header('content-type', page.content_type)
                    self.end_headers()
                    self.wfile.write(content)
                else:
                    self.end_headers()

        self._server = BaseHTTPServer.HTTPServer((self._host, self._port), RequestHandler)
        self._pages = {}
        self._thread = WebServerThread(self._server)

    @property
    def url(self):
        return self._url

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *exc):
        self._server.shutdown()
        self._thread.join()

    def page(self, url):
        import urllib
        if url not in self._pages:
            full_url = urllib.basejoin(self.url, url)
            self._pages[url] = Page(full_url)
        return self._pages[url]

    def set(self, url, content, content_type='text/plain'):
        page = self.page(url)
        page.set_content(content, content_type)
        return page


class Page(object):
    def __init__(self, url):
        self.url = url
        self._content = ''
        self._status = 200
        self._status_message = 'OK'
        self._content_type = ''
        self._requests = []

    def set_content(self, content, content_type):
        self._content = content
        self._content_type = content_type

    @property
    def status(self):
        return self._status

    @property
    def status_message(self):
        return self._status_message

    @property
    def content_type(self):
        return self._content_type

    @property
    def content(self):
        return self._content

    def _record_request(self, request):
        self._requests.append(request)

    def request(self, index):
        assert len(self._requests) >= index
        return self._requests[index-1]


class WebServerThread(Thread):
    def __init__(self, server):
        self.server = server
        super(WebServerThread, self).__init__()
        self.setDaemon(True)

    def run(self):
        self.server.serve_forever(poll_interval=0.05)
