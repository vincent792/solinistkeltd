
from api import keys  

# views.py
from django.shortcuts import render, redirect

from .models import C2BPayments,LNMOnline
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64
import requests

from access_token import get_access_token


def payment(request):
   
    return render(request, 'payment.html')




def generate_timestamp():
    unformatted_date = datetime.now()
    formatted_date = unformatted_date.strftime('%Y%m%d%H%M%S')
    return formatted_date

def encode_password(shortcode, passkey, timestamp):
    data_to_encode = (shortcode + passkey + timestamp)
    encoded_string = base64.b64encode(data_to_encode.encode()).decode("utf-8")
    return encoded_string



def initiate_stk_push(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')

        # Check if the phone_number is 10 characters long
        if len(phone_number) == 10:
            # Remove the starting zero and add "+254" at the beginning
            phone = '254' + phone_number[1:]
            print(phone)
        else:
            print("Invalid number")
            return

        try:
            timestamp = generate_timestamp()
            password = encode_password(keys.shortCode, keys.passkey, timestamp)
            access_token = get_access_token()

            # STK Push Request
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {
                "Authorization": "Bearer %s" % access_token
            }
            request_data = {
                "BusinessShortCode": keys.shortCode,
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,
                "PartyA": phone,  # Use the user's phone number
                "PartyB": keys.shortCode,
                "PhoneNumber": phone,  # Use the user's phone number
                "CallBackURL": "https://solinistkeltd-vincent792.vercel.app/api/lipanampesa/",
                "AccountReference": "test",
                "TransactionDesc": "test"
            }

            response = requests.post(api_url, json=request_data, headers=headers)
            response_data = response.json()
            print(response_data)

            return redirect('payment_success')  # Redirect to a payment success page
        except Exception as e:
            return render(request, 'error.html', {'error_message': str(e)})

    return render(request, 'error.html', {'error_message': 'Invalid request method'})



def payment_success(request):
    return render(request, 'payment_success.html')






from rest_framework.generics import CreateAPIView

from rest_framework.permissions import AllowAny

from .models import LNMOnline
from api.serializer import LNMOnlineSerializer
from rest_framework import serializers


class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(request.data, "this is request.data")

        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        print(merchant_request_id, "this should be MerchantRequestID")
        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        result_code = request.data["Body"]["stkCallback"]["ResultCode"]
        result_description = request.data["Body"]["stkCallback"]["ResultDesc"]
        amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0][
            "Value"
        ]
        print(amount, "this should be an amount")
        mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"][
            "Item"
        ][1]["Value"]
        print(mpesa_receipt_number, "this should be an mpesa_receipt_number")

        balance = ""
        transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"][
            "Item"
        ][3]["Value"]
        print(transaction_date, "this should be an transaction_date")

        phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][
            4
        ]["Value"]
        print(phone_number, "this should be an phone_number")

        from datetime import datetime

        str_transaction_date = str(transaction_date)
        print(str_transaction_date, "this should be an str_transaction_date")

        transaction_datetime = datetime.strptime(str_transaction_date, "%Y%m%d%H%M%S")
        print(transaction_datetime, "this should be an transaction_datetime")

        import pytz
        aware_transaction_datetime = pytz.utc.localize(transaction_datetime)
        print(aware_transaction_datetime, "this should be an aware_transaction_datetime")


        from api.models import LNMOnline

        our_model = LNMOnline.objects.create(
            CheckoutRequestID=checkout_request_id,
            MerchantRequestID=merchant_request_id,
            Amount=amount,
            ResultCode=result_code,
            ResultDesc=result_description,
            MpesaReceiptNumber=mpesa_receipt_number,
            Balance=balance,
            TransactionDate=aware_transaction_datetime,
            PhoneNumber=phone_number,
        )

        our_model.save()

        from rest_framework.response import Response

        return Response({"OurResultDesc": "YEEY!!! It worked!"})

class C2BPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BPayments
        fields = (
        "id",
        "TransactionType",
        "TransID",
        "TransTime",
        "TransAmount",
        "BusinessShortCode",
        "BillRefNumber",
        "InvoiceNumber",
        "OrgAccountBalance",
        "ThirdPartyTransID",
        "MSISDN",
        "FirstName",
        "MiddleName",
        "LastName",
        )




class C2BValidationAPIView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(request.data, "this is request.data in Validation")

        from rest_framework.response import Response
        my_headers = self.get_success_headers(request.data)

        return Response({
            "ResultCode": 1,
            "ResponseDesc":"Failed!"
        },
        headers=my_headers)

class C2BConfirmationAPIView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(request.data, "this is request.data in Confirmation")

        """
        {'TransactionType': 'Pay Bill', 
        'TransID': 'NCQ61H8BK4',
         'TransTime': '20190326210441',
          'TransAmount': '2.00', 
          'BusinessShortCode': '601445',
           'BillRefNumber': '12345678', 
           'InvoiceNumber': '', 
           'OrgAccountBalance': '18.00', 
           'ThirdPartyTransID': '', 
           'MSISDN': '254708374149', 
           'FirstName': 'John', 
           'MiddleName': 'J.', 
           'LastName': 'Doe'
           } 
           this is request.data in Confirmation
           """


        from rest_framework.response import Response

        return Response({"ResultDesc": 0})


