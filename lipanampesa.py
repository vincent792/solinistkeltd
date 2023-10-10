import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import keys
import base64

# Working on time stamp
unformatted_date = datetime.now()
formatted_date = unformatted_date.strftime('%Y%m%d%H%M%S')
print("Formatted", formatted_date)
# password
data_to_encode = (
        keys.shortCode + keys.passkey + formatted_date
    )

encoded_string = base64.b64encode(data_to_encode.encode())
print(encoded_string) 

decoded_password = encoded_string.decode("utf-8")

# Access token
consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
json_response = r.json()
my_access_token = json_response['access_token']
print(my_access_token)

# Function to initiate Lipa Na M-Pesa
def lipa_na_mpesa():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {
        "Authorization": "Bearer %s" % access_token
    }
    request = {
        "BusinessShortCode": keys.shortCode,
        "Password":decoded_password,
        "Timestamp": formatted_date,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": "254700900609",
        "PartyB": keys.shortCode,
        "PhoneNumber": "254700900609",
        "CallBackURL": "",
        "AccountReference": "Test",
        "TransactionDesc": "Test"
    }

    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)

# Call the function to initiate Lipa Na M-Pesa
lipa_na_mpesa()
