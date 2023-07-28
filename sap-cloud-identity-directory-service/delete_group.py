import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .constants import GROUP_ENDPOINT
from .utils import basic_auth
from .utils import base_url
logger = get_logger(LOGGER_NAME)


def delete_group(config, params):
    try:
        url = base_url(config) + GROUP_ENDPOINT + params.get("groupUUID")
        HEADER = basic_auth(config)
        res = requests.delete(url, headers=HEADER, timeout=10)
        eval_response(res)
    except Exception as e:
        raise ConnectorError(e)