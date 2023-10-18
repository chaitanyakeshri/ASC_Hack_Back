from django.shortcuts import render

# Create your views here.
from .models import Scanner, Event, User
from .serializers import EventSerializer, ScannerSerializer, UserSerializer,EventUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework import request

""" Data to be fetched once a day when internet access  is given"""

@api_view(["GET"])
def fetch_data(request ):
    date = request.data['date']
    event = request.data['token']
    data =  Event.objects.filter(date = date, token = event)
    serializer= EventSerializer(data, many = True)
    return Response(serializer.data)


@api_view(["POST"])
def scanner_login(request):
    login_id = request.data['scanner']
    password = request.data['password']
    try:
        scanner = Scanner.objects.get(login_id=login_id)
    except Scanner.DoesNotExist:
        return Response({"message": "scanner does not exist"}, status=status.HTTP_404_NOT_FOUND)
    if  scanner.password != password:
        return Response({"message": "invalid login"}, status=status.HTTP_401_UNAUTHORIZED)
    serializer = EventSerializer(scanner)
    return Response(serializer.data, status=status.HTTP_200_OK)

"""
@api_view(["PUT"])
def entry_check(request, login_id):
    try:
        user = User.objects.get(pk=login_id)
    except User.DoesNotExist:
        return Response({"message": "user does not exist"})
    user.entry = datetime.now()
    serializer = UserSerializer(user.login_id)
    if user.entry < user.entry_date or user.entry > user.exit_date:
        return Response({"0"})
    else:
        user.campus_entry = True
        return Response(serializer.data)

"""
"""
@api_view(["PUT"])
def exit_check(request, login_id):
    user = User.objects.get(pk=login_id)
    user.exit = datetime.now()
    serializer = UserSerializer(user.login_id)
    return Response(serializer.data)

"""
"""
@api_view(["PUT"])
def event_check(request, token, login_id):
    try:
        user = User.objects.get(pk=login_id)
        event = Event.objects.get(pk=token)
    except Event.DoesNotExist or User.DoesNotExist:
        return Response({"message": "does not exist"})
    for i in user.events:
        if user.events[i] == token:
            user.events_verified[i] = True
            return Response({"message": "entry verified"})
    return Response({"message": "entry denied"})
"""