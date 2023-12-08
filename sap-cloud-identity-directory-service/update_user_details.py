from connectors.core.connector import get_logger
from .constants import LOGGER_NAME, USER_ENDPOINT
from .utils import make_rest_api_call
logger = get_logger(LOGGER_NAME)


def update_user_details(config, params):
    def build_operation_object(operation_name, path, value=None):
        _operation = {
            "op": operation_name,
        }
        if path:
            _operation["path"] = path
        if value:
            _operation["value"] = value
        return _operation

    endpoint = USER_ENDPOINT + str(params.get("userUUID"))
    body_data = {
        "schemas": [
            "urn:ietf:params:scim:api:messages:2.0:PatchOp"
        ]
    }
    all_operations = []
    status = params.get('status', '')
    if status:
        status_op = build_operation_object('replace', 'active', status == 'Active')
        all_operations.append(status_op)
    op = params.get('operations')
    if op == 'Add Attribute':
        all_operations.append(build_operation_object('add', params.get('path'), params.get('value')))
    elif op == 'Replace Attribute':
        all_operations.append(build_operation_object('replace', params.get('path'), params.get('value')))
    elif op == 'Remove Attribute':
        all_operations.append(build_operation_object('remove', params.get('path')))
    additional_operations = params.get("add_operations")
    if additional_operations:
        all_operations.extend(additional_operations)
    body_data['Operations'] = all_operations
    response = make_rest_api_call(config, endpoint, method='PATCH', json=body_data)
    response['message'] = 'The user is updated successfully.'
    response['status'] = 204
    if 'Resources' in response and not response.get('Resources'):
        response.pop('Resources')
    return response
