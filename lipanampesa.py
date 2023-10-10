import requests

from datetime import datetime
import keys
import base64
from access_token import get_access_token

def generate_timestamp():
    unformatted_date = datetime.now()
    formatted_date = unformatted_date.strftime('%Y%m%d%H%M%S')
    return formatted_date

def encode_password(shortcode, passkey, timestamp):
    data_to_encode = (shortcode + passkey + timestamp)
    encoded_string = base64.b64encode(data_to_encode.encode()).decode("utf-8")
    return encoded_string



def lipa_na_mpesa():
    timestamp = generate_timestamp()
    password = encode_password(keys.shortCode, keys.passkey, timestamp)
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {
        "Authorization": "Bearer %s" % access_token
    }
    request = {
        "BusinessShortCode": keys.shortCode,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": "254758203298",
        "PartyB": keys.shortCode,
        "PhoneNumber": "254758203298",
        "CallBackURL": "https://solinistkeltd-vincent792.vercel.app/api/lipanampesa/",
        "AccountReference": "Test",
        "TransactionDesc": "Test"
    }
    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)

# Call the function to initiate Lipa Na M-Pesa
lipa_na_mpesa()
