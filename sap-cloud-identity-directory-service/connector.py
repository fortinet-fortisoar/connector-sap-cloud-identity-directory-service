from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from .builtins import *
from .utils import make_rest_api_call
from .constants import LOGGER_NAME, PASSWORD_SERVICE
logger = get_logger(LOGGER_NAME)


class Sapias(Connector):
    def execute(self, config, operation, params, *args, **kwargs):
        try:
            return supported_operations.get(operation)(config, params)
        except Exception as err:
            logger.exception(err)
            raise ConnectorError(err)

    def check_health(self, config):
        try:
            response = make_rest_api_call(config, PASSWORD_SERVICE, method='POST')
            logger.info("connector is available")
            return True
        except Exception as err:
            logger.exception(err)
            raise ConnectorError(err)
