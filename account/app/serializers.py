from rest_framework import serializers
from .models import *

from rest_framework.response import Response


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class SendSmsSerializer(serializers.Serializer):
    fromSms = serializers.CharField()
    to = serializers.CharField()
    text = serializers.CharField()
   