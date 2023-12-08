"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""
from connectors.core.connector import get_logger
from .constants import LOGGER_NAME, USER_ENDPOINT
from .utils import make_rest_api_call

logger = get_logger(LOGGER_NAME)


def create_user(config, params):
    user_details = {
        "userName": params.get("userName", ""),
        "schemas": [
            "urn:ietf:params:scim:schemas:core:2.0:User"
        ],
        "name": {
            "givenName": params.get("givenName", ""),
            "familyName": params.get("familyName", ""),
        },
        "userType": params.get("userType", ""),
        "emails": [
            {
                "value": params.get("email"),
                "primary": params.get("primary", True)
            }
        ]
    }
    body_data = params.get("userDetails")
    if body_data:
        body_data_copy = body_data.copy()
        for k, v in body_data_copy.items():
            if user_details.get(k):
                if isinstance(v, dict):
                    user_details[k].update(body_data.pop(k, {}))
                elif isinstance(v, list):
                    user_details[k].extend(body_data.pop(k, []))
        user_details.update(body_data)
    response = make_rest_api_call(config, endpoint=USER_ENDPOINT, method='POST', json=user_details)
    response['message'] = 'The user is updated successfully.'
    response['status'] = 204
    if 'Resources' in response and not response.get('Resources'):
        response.pop('Resources')
    return response
