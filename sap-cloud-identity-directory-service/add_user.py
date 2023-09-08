import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .constants import USER_ENDPOINT
from .utils import basic_auth
from .utils import base_url
logger = get_logger(LOGGER_NAME)


def add_user(config, params):
    try:
        url = base_url(config) + USER_ENDPOINT
        HEADER = basic_auth(config)
        body_data = params.get("userDetails")
        res = requests.post(url, headers=HEADER, json=body_data, timeout=10)
        return res.json()
    except Exception as e:
        raise ConnectorError(e)