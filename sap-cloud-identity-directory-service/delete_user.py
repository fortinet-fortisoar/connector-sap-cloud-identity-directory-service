import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .constants import USER_ENDPOINT
from .utils import basic_auth
from .utils import base_url
from .utils import eval_response
logger = get_logger(LOGGER_NAME)


def delete_user(config, params):
    try:
        url = base_url(config) + USER_ENDPOINT + str(params.get("userUUID"))
        HEADER = basic_auth(config)
        res = requests.delete(url, headers=HEADER, timeout=10)
        return eval_response(res)
    except Exception as e:
        raise ConnectorError(e)