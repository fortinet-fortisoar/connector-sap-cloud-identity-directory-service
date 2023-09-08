from connectors.core.connector import get_logger
from .constants import LOGGER_NAME, USER_ENDPOINT
from .utils import make_rest_api_call
logger = get_logger(LOGGER_NAME)


def delete_user(config, params):
    endpoint = USER_ENDPOINT + str(params.get("userUUID"))
    response = make_rest_api_call(config, endpoint, method='DELETE')
    response['message'] = 'The user is deleted successfully.'
    response['status'] = 204
    if 'Resources' in response and not response.get('Resources'):
        response.pop('Resources')
    return response
