from .models import User, Event
from .serializers import UserSerializer, EventSerializer, User_EventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework import request


@api_view(["POST"])
def user_login(request):
    login_id = request.data["user"]
    password = request.data["password"]
    #device_number=request.data["user"]
    try:
        user = User.objects.get(login_id=login_id)
    except User.DoesNotExist:
        return Response({"message": "scanner does not exist"}, status=status.HTTP_404_NOT_FOUND)
    if user.password != password:  
        return Response({"message": "invalid login"}, status=status.HTTP_401_UNAUTHORIZED)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)




"""
@api_view(["GET"])
def entry_exit_qr(request):
    login_id = request.data["user"]
    user = User.objects.get(pk=login_id)
    serializer = UserSerializer(user.login_id)
    return Response(serializer.data)

"""
@api_view(["GET"])
def event_qr(request):
     login_id = request.data["user"]
     user = User.objects.get(pk=login_id)
     Tickets = {}
     key_index = 0
     for i in user.events:
         Tickets[key_index] = i
         key_index+= 1
     return Response(Tickets)
        
"""
@api_view(["PUT"])
def event_verified(request, token):
    login_id = request.data["user"]
    user = User.objects.get(pk=login_id)
    for i in user.events:
        if user.events[i] == token:
            user.events_verified[i] = True
            user.events[i] = None
            break
    return Response({"message": "entry verified"})
"""