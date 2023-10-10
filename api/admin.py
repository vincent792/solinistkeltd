from django.contrib import admin

# Register your models here.
from  api.models import UserProfile, LNMOnline
admin.site.register(UserProfile)


class LNMOnlineAdmin(admin.ModelAdmin):
    list_display = ("PhoneNumber", "Amount", "MpesaReceiptNumber", "TransactionDate")

admin.site.register(LNMOnline,LNMOnlineAdmin)