from requests.auth import HTTPBasicAuth #for   access token
import requests
# accss token
consumer_key='lpsOiOiQoy7HqJFYdUXZ6VRm4LXGT2AM'
consumer_secret= 'mSeGFbrx1PeZW6ar'
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
print("Text Respose", r.text)
print("Json Response", r.json())

json_response=r.json()
access_token=json_response['access_token']
print("Access Token", access_token)
