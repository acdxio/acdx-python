from acdx.rest_api import RestApi
from acdx.ws_api import WebSocketApi
from acdx.utils import AcdxApiException

def rest_api_examples():
    api = RestApi('your_api_key', 'your_b64_secret')
    try:
        res = api.get_account()
    except AcdxApiException as err:
        print(err)
    except Exception as err:
        print("Exception raised: {}".format(err))
    else:
        print(res)


def ws_api_examples():
    api = WebSocketApi('your_api_key', 'your_b64_secret')
    channels = ["orders", "trading"]
    api.subscribe(["ETHH19"], channels)

    while True:
        try:
            print(api.receive_msg())
        except AcdxApiException as err:
            print(err)
            break
        except Exception as err:
            print("Exception raised: {}".format(err))
            break


if __name__ == "__main__":
    rest_api_examples()
    ws_api_examples()
