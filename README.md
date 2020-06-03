# API Client for [ACDX API](https://docs.acdx.io/)

## Description

[ACDX API client](https://www.acdx.io/) is available in this package.

### Example

```
See examples.py file

or

from acdx.rest_api import RestApi
acdx_client = RestApi("your_api_key", "your_b64_secret")
result = acdx_client.get_account()
print(result)
