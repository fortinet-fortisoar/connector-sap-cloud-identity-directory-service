import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .constants import GROUP_ENDPOINT
from .utils import basic_auth
from .utils import base_url
logger = get_logger(LOGGER_NAME)


def get_group_details(config, params):
    try:
        if params.get("filter"):
            url = base_url(config) + GROUP_ENDPOINT + "?filter=" + params.get("filter")
        else:
            url = base_url(config) + GROUP_ENDPOINT
        HEADER = basic_auth(config)
        res = requests.get(url, headers=HEADER, timeout=10)
        return res.json()
    except Exception as e:
        raise ConnectorError(e)