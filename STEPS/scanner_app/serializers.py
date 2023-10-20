from rest_framework import serializers
from .models import Event,Scanner,User

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields="__all__"


class ScannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Scanner
        fields=["event"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["users"]