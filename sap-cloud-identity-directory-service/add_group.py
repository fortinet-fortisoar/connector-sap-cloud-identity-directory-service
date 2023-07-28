import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .constants import GROUP_ENDPOINT
from .utils import basic_auth
from .utils import base_url
logger = get_logger(LOGGER_NAME)


def add_group(config, params):
    try:
        url = base_url(config) + GROUP_ENDPOINT
        HEADER = basic_auth(config)
        if len(params.get("name")) > 0:
            body_data = {
                "schemas": [
                    "urn:ietf:params:scim:schemas:core:2.0:Group"
                ],
                "displayName": params.get("name"),
            }
        else:
            body_data = params.get("customJSON")
        res = requests.post(url, headers=HEADER, json=body_data, timeout=10)
        return res.json()
    except Exception as e:
        raise ConnectorError(e)