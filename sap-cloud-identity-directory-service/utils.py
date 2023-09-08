import base64
import requests
from .constants import REQUEST_TIMEOUT, LOGGER_NAME
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger(LOGGER_NAME)


def make_rest_api_call(config, endpoint, method='GET', header={}, **kwargs):
    try:
        url = "https://" + config.get("tenantID") + ".accounts.ondemand.com" + endpoint
        creds = config.get("clientID") + ":" + config.get("clientSecret")
        basic_auth = base64.b64encode(creds.encode("ascii"))
        headers = {
            "Authorization": "Basic " + basic_auth.decode("ascii"),
            "Content-Type": "application/scim+json"
        }
        headers.update(header)
        response = requests.request(method, url, timeout=REQUEST_TIMEOUT, verify=True, headers=headers, **kwargs)
        if response.ok:
            if response.status_code == 204:
                return {"status": 204}
            return response.json()
        elif response.status_code == 404 and response.headers.get('Content-Type') == 'application/json':
            logger.debug("Error: {0}".format(response.json()))
            return {'Resources': []}
        else:
            try:
                logger.error("Error: {0}".format(response.json()))
                raise ConnectorError('Error: {0}'.format(response.json()))
            except Exception as error:
                raise ConnectorError('{0}'.format(response.text if response.text else str(response)))
    except requests.exceptions.SSLError as e:
        logger.exception('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))
    except requests.exceptions.ConnectionError as e:
        logger.exception('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))
    except Exception as e:
        logger.error('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))
