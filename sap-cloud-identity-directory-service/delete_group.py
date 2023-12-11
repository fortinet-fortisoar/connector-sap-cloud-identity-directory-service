"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""
from connectors.core.connector import get_logger
from .constants import LOGGER_NAME
from .constants import GROUP_ENDPOINT
from .utils import make_rest_api_call
logger = get_logger(LOGGER_NAME)


def delete_group(config, params):
    endpoint = GROUP_ENDPOINT + params.get("group_id")
    response = make_rest_api_call(config, endpoint, method='DELETE')
    response['message'] = 'The group is deleted successfully.'
    response['status'] = 204
    if 'Resources' in response and not response.get('Resources'):
        response.pop('Resources')
    return response
