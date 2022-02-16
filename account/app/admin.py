from django.contrib import admin
from app.models import Account, Phone_number,SendSms


class Accountadmin(admin.ModelAdmin):
    list_display = ('id','auth_id','username')
admin.site.register(Account,Accountadmin)

class Phone_numberadmin(admin.ModelAdmin):
    list_display =('id','account_id','number')
admin.site.register(Phone_number,Phone_numberadmin)

class SendSmsadmin(admin.ModelAdmin):
    list_display =('fromSms','to','text')
admin.site.register(SendSms,SendSmsadmin)