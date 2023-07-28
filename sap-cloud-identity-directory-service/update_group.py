import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .constants import GROUP_ENDPOINT
from .utils import basic_auth
from .utils import base_url
from .utils import eval_response
logger = get_logger(LOGGER_NAME)


def update_group(config, params):
    try:
        url = base_url(config) + GROUP_ENDPOINT + params.get("groupUUID")
        HEADER = basic_auth(config)
        if params.get("addUser"):
            body_data = {
                "schemas": [
                    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
                ],
                "Operations": [
                    {
                    "op": "add",
                    "path": "members",
                    "value": [
                        {
                        "value": params.get("userUUID")
                        }
                        ]
                    }
                ]
            }

        elif params.get("removeUser"):
            body_data = {
                "schemas": [
                    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
                ],
                "Operations": [
                    {
                    "op": "remove",
                    "path": "members[value eq \"" + params.get("userUUID") + "\"]"
                    }
                ]
            }

        else:
            body_data = params.get("customJSON")

        res = requests.patch(url, headers=HEADER, json=body_data, timeout=10)
        eval_response(res)
    except Exception as e:
        raise ConnectorError(e)