# Mock Web Server

[![CircleCI](https://circleci.com/gh/Virtualstock/mockwebserver.svg?style=svg&circle-token=a157be22d8ba5cd2fefe5517bc8de839b7cd232e)](https://circleci.com/gh/Virtualstock/mockwebserver)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Virtualstock_mockwebserver&metric=alert_status)](https://sonarcloud.io/dashboard?id=Virtualstock_mockwebserver)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Virtualstock_mockwebserver&metric=coverage)](https://sonarcloud.io/dashboard?id=Virtualstock_mockwebserver)
[![pullreminders](https://pullreminders.com/badge.svg)](https://pullreminders.com?ref=badge)

A simple web server for unit testing purposes. Acts as context manager for teardown.

## How to develop

```
pip install -r requirements.txt
```

## How to use

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


## How to distribute

If you need to publish a new version of this package you can use this command:

```bash
$ make build
$ make dist
```


# License

Licensed under `MIT license`. View [license](LICENSE).
