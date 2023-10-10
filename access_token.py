import requests
from requests.auth import HTTPBasicAuth
import keys

def get_access_token():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_response = response.json()
    return json_response.get('access_token')

get_access_token()