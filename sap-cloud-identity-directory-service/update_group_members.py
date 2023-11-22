from connectors.core.connector import get_logger
from .constants import LOGGER_NAME
from .constants import GROUP_ENDPOINT
from .utils import make_rest_api_call

logger = get_logger(LOGGER_NAME)


def update_group_members(config, params):
    def get_member_list(members):
        if isinstance(members, (list, tuple)):
            members = list(members)
        elif isinstance(members, str):
            members = members.split(",")
        member_list = []
        for mem in members:
            member_list.append({"value": mem.strip()})
        return member_list

    def get_attribute_path(user_ids):
        if isinstance(user_ids, (list, tuple)):
            members = list(user_ids)
        elif isinstance(user_ids, str):
            members = user_ids.split(",")
        path_strings = []
        for mem in members:
            path_strings.append("members[value eq \"{0}\"]".format(mem.strip()))
        return " or ".join(path_strings)
    endpoint = GROUP_ENDPOINT + params.get("group_id")
    body_data = {
        "schemas": [
            "urn:ietf:params:scim:api:messages:2.0:PatchOp"
        ]
    }
    op = params.get('operation')
    operations = []
    if op == 'Add Members':
        operation = {
            "op": 'add',
            "path": "members",
            "value": get_member_list(params.get("user_uuids"))
        }
    elif op == 'Replace Members':
        operation = {
            "op": 'replace',
            "path": get_attribute_path(params.get('user_path')),
            "value": get_member_list(params.get("user_uuids"))
        }
    else:
        operation = {
                    "op": "remove",
                    "path": get_attribute_path(params.get('user_uuids'))
                }
    operations.append(operation)
    body_data['Operations'] = operations
    response = make_rest_api_call(config, endpoint, method='PATCH', json=body_data)
    response['message'] = 'The group is updated successfully.'
    response['status'] = 204
    if 'Resources' in response and not response.get('Resources'):
        response.pop('Resources')
    return response
