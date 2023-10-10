import requests

import keys

from access_token import get_access_token

def make_api_request(url, request_data, access_token):
    headers = {"Authorization": "Bearer %s" % access_token}
    try:
        response = requests.post(url, json=request_data, headers=headers)
        print(response.text)
    except:
        response = requests.post(url, json=request_data, headers=headers, verify=False)
        print(response.text)

def register_url():
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    request_data = {
        "ShortCode": keys.shortcode,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://solinistkeltd-vincent792.vercel.app/api/c2b-confirmation/",
        "ValidationURL": "https://solinistkeltd-vincent792.vercel.app/api/c2b-validation/",
    }
    make_api_request(api_url, request_data, access_token)
# register_url()

def simulate_c2b_transaction():
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    request_data = {
        "ShortCode": keys.shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "2",
        "Msisdn": keys.test_msisdn,
        "BillRefNumber": "12345678",
    }
    make_api_request(api_url, request_data, access_token)

# Call the functions to perform the actions

simulate_c2b_transaction()
