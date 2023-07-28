from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from django.utils.module_loading import import_string
from .builtins import *
from .constants import LOGGER_NAME
from .constants import PASSWORD_SERVICE
import base64
import requests
logger = get_logger(LOGGER_NAME)


class Sapias(Connector):

    def execute(self, config, operation, params, *args, **kwargs):
        return supported_operations.get(operation)(config, params)

    def check_health(self, config):
        try:
            url = "https://" + config.get("tenantID") + ".accounts.ondemand.com" + PASSWORD_SERVICE
            creds = config.get("clientID") + ":" + config.get("clientSecret")
            basic_auth = base64.b64encode(creds.encode("ascii"))
            PASSWORD_SERVICE_HEADER = {
                "Authorization" : "Basic " + basic_auth.decode("ascii"),
                "Content-Type" : "application/json",
            }
            res = requests.post(url, headers=PASSWORD_SERVICE_HEADER, timeout=10)
            if res.status_code == 200:
              return True
            else:
              raise ConnectorError(e)
        except Exception as e:
            raise ConnectorError(e)