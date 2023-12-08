"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""
from connectors.core.connector import get_logger
from .constants import LOGGER_NAME, GROUP_ENDPOINT
from .utils import make_rest_api_call

logger = get_logger(LOGGER_NAME)


def create_group(config, params):
    def get_members_list(_members):

        members_list = _members if isinstance(_members, (list, tuple)) else _members.split(',')
        result = []
        for member in members_list:
            mem = {
                "value": member.strip(),
                "type": "User"
            }
            result.append(mem)
        return result
    endpoint = GROUP_ENDPOINT
    body_data = {
        "schemas": [
            "urn:ietf:params:scim:schemas:core:2.0:Group",
            "urn:sap:cloud:scim:schemas:extension:custom:2.0:Group"
        ],
        "displayName": params.get("displayName"),
        "urn:sap:cloud:scim:schemas:extension:custom:2.0:Group": {
            "name": params.get("name"),
            "description": params.get("description")
        }
    }
    if params.get("externalId"):
        body_data["externalId"] = params.get("externalId")
    members = params.get('members')
    if members:
        body_data["members"] = get_members_list(members)
    response = make_rest_api_call(config, endpoint, method='POST', json=body_data)
    return response
