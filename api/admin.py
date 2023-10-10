from django.contrib import admin

# Register your models here.
from  api.models import UserProfile, LNMOnline,C2BPayments
admin.site.register(UserProfile)


class LNMOnlineAdmin(admin.ModelAdmin):
    list_display = ("PhoneNumber", "Amount", "MpesaReceiptNumber", "TransactionDate")

admin.site.register(LNMOnline,LNMOnlineAdmin)


class C2BPaymentsAdmin(admin.ModelAdmin):
    list_display = ("MSISDN", "TransAmount", "TransID", "TransTime")

admin.site.register(C2BPayments,C2BPaymentsAdmin)