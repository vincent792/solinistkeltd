# models.py
from django.db import models
from  django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=23,  null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    # Add other fields as needed
    def __str__(self) -> str:
        return self.name


class LNMOnline(models.Model):
    CheckoutRequestID = models.CharField(max_length=50, blank=True, null=True)
    MerchantRequestID = models.CharField(max_length=20, blank=True, null=True)
    ResultCode = models.IntegerField(blank=True, null=True)
    ResultDesc = models.CharField(max_length=120, blank=True, null=True)
    Amount = models.FloatField(blank=True, null=True)
    MpesaReceiptNumber = models.CharField(max_length=15, blank=True, null=True)
    Balance = models.CharField(max_length=12, blank=True, null=True)
    TransactionDate = models.DateTimeField(blank=True, null=True)
    PhoneNumber = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return f"{self.PhoneNumber} has sent {self.Amount} >> {self.MpesaReceiptNumber}"
    


class C2BPayments(models.Model):
    TransactionType =  models.CharField(max_length=12, blank=True, null=True)
    TransID = models.CharField(max_length=12, blank=True, null=True)
    TransTime = models.CharField(max_length=14, blank=True, null=True)
    TransAmount = models.CharField(max_length=12, blank=True, null=True)
    BusinessShortCode = models.CharField(max_length=6, blank=True, null=True)
    BillRefNumber = models.CharField(max_length=20, blank=True, null=True)
    InvoiceNumber = models.CharField(max_length=20, blank=True, null=True)
    OrgAccountBalance = models.CharField(max_length=12, blank=True, null=True)
    ThirdPartyTransID = models.CharField(max_length=20, blank=True, null=True)
    MSISDN = models.CharField(max_length=12, blank=True, null=True)
    FirstName = models.CharField(max_length=20, blank=True, null=True)
    MiddleName = models.CharField(max_length=20, blank=True, null=True)
    LastName = models.CharField(max_length=20, blank=True, null=True)
