from django.shortcuts import render

from rest_framework.views import APIView

from django.contrib.auth import authenticate,login

from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import ProfileSerializer

from planner.utils import generate_password,send_email

import threading

# from django.contrib.auth.hashers import make_password

# Create your views here.



class LoginView(APIView):

    def post(self,request,*args,**kwargs):

        username = request.data.get('username')

        password = request.data.get('password')

        user = authenticate(username = username,password = password)

        if user :

                refresh_token = RefreshToken.for_user(user)

                access_token = refresh_token.access_token

                data  = {'refresh_token':str(refresh_token),'access_token':str(access_token)}

                return Response(data,status=200)

        data = {'msg': 'invalid username'}

        return Response(data,status=400)


class UserRegisterView(APIView):

    def post(self,request,*args,**kwargs):

        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():

            username = serializer.validated_data.get('username')
             
            profile = serializer.save()

            profile.email = username

            

            password = generate_password()

            # profile.password = password

            profile.set_password(password)

            profile.save()

            recipient = profile.email

            subject = 'Cake Site-Login Credentials'

            context = {'name' : profile.first_name, 'username' : profile.username,'password' : password }

            template = 'emails/credentials.html'

            # send_email(recipient,subject,context,template)

            thread=threading.Thread(target=send_email,args=(recipient,subject,context,template))

            thread.start()

            data = {'msg':'account created'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

