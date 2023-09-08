from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME, USER_ENDPOINT
from .utils import make_rest_api_call
logger = get_logger(LOGGER_NAME)


def get_user_list(config, params):
    query_param = {}
    count = params.pop('count', '')
    start_id = params.pop('start_id', 'initial')
    if start_id:
        query_param['startId'] = start_id
    if count != "":
        query_param['count'] = count
    _filter = params.pop('filter', '')
    query_list = []
    for k, v in params.items():
        if v:
            if k == 'userType':
                v = v.lower()
            query_list.append('{0} eq "{1}"'.format(k, v))
    if _filter:
        query_list.append(_filter)
    query_string = " and ".join(query_list)
    if query_string:
        query_param.update({'filter': query_string})
    response = make_rest_api_call(config, USER_ENDPOINT, params=query_param)
    return response
