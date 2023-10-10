import requests
from requests.auth import HTTPBasicAuth


import keys

def register_url():

    # Access token
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_response = r.json()
    my_access_token = json_response['access_token']
    # print(my_access_token)

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {
        "ShortCode": keys.shortcode,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://django-mpesa-vincent792.vercel.app/api/c2b-confirmation/",
        "ValidationURL":   "https://django-mpesa-vincent792.vercel.app/api/lipanampesa/c2b-validation/",
    }

    
    response = requests.post(api_url, json=request, headers=headers)
   

    print(response.text)


register_url()


# def simulate_c2b_transaction():
#     my_access_token = generate_access_token()

#     api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

#     headers = {"Authorization": "Bearer %s" % my_access_token}

#     request = {
#         "ShortCode": keys.shortcode,
#         "CommandID": "CustomerPayBillOnline",
#         "Amount": "4",
#         "Msisdn": keys.test_msisdn,
#         "BillRefNumber": "myaccnumber",
#     }
#     try:
#         response = requests.post(api_url, json=request, headers=headers)

#     except:
#         response = requests.post(api_url, json=request, headers=headers, verify=False)

#     print(response.text)


# simulate_c2b_transaction()