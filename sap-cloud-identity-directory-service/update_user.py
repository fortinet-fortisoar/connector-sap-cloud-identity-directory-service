import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .constants import USER_ENDPOINT
from .utils import basic_auth
from .utils import base_url
from .utils import eval_response
logger = get_logger(LOGGER_NAME)


def update_user(config, params):
    try:
        url = base_url(config) + USER_ENDPOINT + str(params.get("userUUID"))
        HEADER = basic_auth(config)
        if params.get("enable"):
            body_data = {
                "schemas": [
                    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
                ],
                "Operations": [
                    {
                    "op": "replace",
                    "path": "active",
                    "value": True
                    }
                ]
            }

        elif params.get("disable"):
            body_data = {
                "schemas": [
                    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
                ],
                "Operations": [
                    {
                    "op": "replace",
                    "path": "active",
                    "value": False
                    }
                ]
            }

        else:
            body_data = params.get("customJSON")
        
        res = requests.patch(url, headers=HEADER, json=body_data, timeout=10)
        eval_response(res)
    except Exception as e:
        raise ConnectorError(e)