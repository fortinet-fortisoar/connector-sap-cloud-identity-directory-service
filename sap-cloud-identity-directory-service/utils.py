import base64

# basic auth header creation
def basic_auth(config):
	creds = config.get("clientID") + ":" + config.get("clientSecret")
	basic_auth = base64.b64encode(creds.encode("ascii"))
	header = {
	"Authorization" : "Basic " + basic_auth.decode("ascii"),
	"Content-Type" : "application/scim+json"
	}
	return header

# url base creation
def base_url(config):
	url = "https://" + config.get("tenantID") + ".accounts.ondemand.com"
	return str(url)

# evaluate response
def eval_response(request_response):
	if request_response.status_code == 204:
		return request_response.status_code
	else:
		return request_response.json()