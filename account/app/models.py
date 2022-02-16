from django.db import models
from django.db.models.fields import CharField, TextField, reverse_related
from django.contrib.auth.models import User, auth

class Account(models.Model):
    id =models.AutoField(primary_key=True)
    auth_id = models.IntegerField(default = 1,unique=True)
    username = models.CharField(max_length=550, default='NA')
    
    def __str__(self):
        return str(self.username)

class Phone_number(models.Model):
    id =models.AutoField(primary_key=True)
    number = models.CharField(max_length=50, null=True, blank=True, unique=True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, default = 1)

    def __str__(self):
        return str(self.number)

class SendSms(models.Model):
    fromSms = models.CharField( min_length= 6,max_length=16, default='NA', null = True, blank=True)
    to = models.CharField( min_length= 6,max_length=16, default='NA', null = True, blank=True)
    text = models.CharField( min_length= 6,max_length=16, default='NA', null = True, blank=True)
