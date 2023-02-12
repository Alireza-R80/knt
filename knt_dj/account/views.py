import jwt
import datetime
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import re

from account.models import Customer, Designer
from account.serializers import UserSerializer, DesignerSerializer


class RegisterView(APIView):
    def post(self, request):
        phone_number_pattern = re.compile(r'^(09)\d{9}$')
        try:
            phone_number = request.data['phone_number']
            password = request.data['password']
        except:
            response = {'message': 'field error'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            if not phone_number:
                response = {'message': 'phone number is required'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

            if not phone_number_pattern.match(phone_number):
                response = {'message': 'phone number is invalid'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

            if not password:
                response = {'message': 'password is required'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            try:
                user = Customer.objects.create_user(phone_number=phone_number, password=password)
            except:
                response = {'message': 'phone number already exists'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        phone_number_pattern = re.compile(r'^(09)\d{9}$')
        phone_number = request.data['phone_number']
        password = request.data['password']
        user = Customer.objects.filter(phone_number=phone_number).first()

        if not phone_number_pattern.match(phone_number):
            response = {'message': 'phone number is invalid'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        if user is None:
            response = {'message': 'user not found'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            response = {'message': 'wrong password'}
            return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        user = get_user(request)
        if user.role == 'CUS':
            serializer = UserSerializer(user)
        elif user.role == 'DES':
            designer = Designer.objects.get(parent_user=user)
            serializer = DesignerSerializer(designer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'logged out successfully'
        }
        return response


def get_user(request):
    token = request.COOKIES.get('jwt')
    if not token:
        response = {'message': 'user not authenticated'}
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        response = {'message': 'user not authenticated'}
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)
    user = Customer.objects.get(id=payload['id'])
    return user


class PromoteView(APIView):

    def post(self, request):
        card_number = request.data['card_number']
        user = get_user(request=request)
        customer = Customer.objects.get(phone_number=user.data['phone_number'])
        customer.role = 'DES'
        customer.save()
        designer = Designer.objects.create(parent_user=customer, card_number=card_number)
        serializer = DesignerSerializer(designer)
        return Response(serializer.data, status=status.HTTP_200_OK)
