# Wavefront API Client

The Wavefront API allows you to perform various operations in Wavefront. The API can be used to automate commonly executed operations such as tagging sources automatically, sending events, and more.

This Python package is automatically generated by the Swagger Codegen project.

- Wavefront API version: 2

If you're looking for the V1 API, the API client can be found in the api-v1 branch of this repository.

## Requirements

- Python 2.7 or higher 
- OpenSSL 1.0.1 or higher (TLSv1.2 support)

**Note ("[Errno 54] Connection reset by peer" error)**:
This is a known issue affecting Python 2.7 on most Macs. macOS ships with an outdated version of the OpenSSL library that only supports deprecated encryption protocols. As a result, Python 2.7 that ships with the system, doesn't support TLSv1.2. During SSL handshake it attempts to use TLSv1 encryption protocol, which is no longer considered secure, and Wavefront servers are terminating the connection, which results in a "Connection reset by peer" error.
To work around this issue, the easiest way would be to install an updated version of Python 2.7 using Homebrew (https://brew.sh), which doesn't rely on the system-provided OpenSSL library, or switch to Python 3.

**Note:** v2.2.x libraries require a minor code modification to be compatible with v2.1.x and earlier versions due to breaking changes introduced by swagger-codegen.
Before:

```python
client = wave_api.ApiClient(host=base_url, header_name='Authorization', header_value='Bearer ' + api_key)
```

After:

```python
config = wave_api.Configuration()
config.host = base_url
client = wave_api.ApiClient(configuration=config, header_name='Authorization', header_value='Bearer ' + api_key)
```

## Setuptools
You can install the bindings via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install
```

Or you can install from Github via pip:

```sh
pip install git+https://github.com/wavefronthq/python-client.git
```

Or you can install from PyPi via pip:

```sh
pip install wavefront_client
```


To use the bindings, import the package:

```python
import wavefront_api_client
```

## Manual Installation
If you do not want to use Setuptools, you can download the latest release.
Then, to use the bindings, import the package:

```python
import path.to.wavefront_api_client
```

## Getting Started

All API endpoints are documented at https://YOUR_INSTANCE.wavefront.com/api-docs/ui/. Below is a simple example demonstrating how to use the library to call the Source API. You can use this example as a starting point.

```python
import wavefront_api_client as wave_api

base_url = 'https://YOUR_INSTANCE.wavefront.com'
api_key = 'YOUR_API_TOKEN'

config = wave_api.Configuration()
config.host = base_url
client = wave_api.ApiClient(configuration=config, header_name='Authorization', header_value='Bearer ' + api_key)

# instantiate source API
source_api = wave_api.SourceApi(client)
sources = source_api.get_all_source()
print sources
```

## Troubleshooting

If you encounter a bug or need help, feel free to leave an [issue](https://github.com/wavefrontHQ/python-client/issues) on this GitHub repository.
