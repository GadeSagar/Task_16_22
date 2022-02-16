from rest_framework.views import APIView
from .models import *
from django.http import JsonResponse
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
#from rest_framework.permissions import AllowAny, IsAuthenticated
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.generics import ListAPIView



class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, auth_id=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'status':'1', 'token':token.key, 'user_id':str(user.id), 'Message':'Login successfully!'}, status=200)
            else:
                return Response({'status':'0', 'Message':'Please give valid username and password'}, status=200)
        else:
            print(serializer.errors)
            return Response({'status':'0', 'Message':'Please give valid username and password'}, status=200)

class SendSms(APIView):
    def post(self, request):
        serializer = SendSmsSerializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            fromSms = data['fromSms']
            to = data['to']
            text = data ['text']
            SendSms_obj= SendSms(fromSms=fromSms, to =to, text = text)
            SendSms_obj.save()
            context = {'status':'1','Message':'SMS add successfully'}
            return Response(context)
        else:
            context = {'status':'0','Message':'SMS add UnSuccessfully'}
            return Response(context)