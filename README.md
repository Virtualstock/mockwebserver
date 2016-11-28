
```
from mockwebserver import MockWebServer()
import requests

def test_requests_get():
    with MockWebServer() as server:
        url = server.set('/path/to/page', "page content")
        response = requests.get(url)
        assert response.ok
        assert response.text = "page content"
```
