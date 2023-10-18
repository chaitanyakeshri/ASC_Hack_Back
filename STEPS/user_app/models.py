from django.db import models
from django import forms


class User(models.Model):
    login_id = models.CharField(primary_key=True, default=None, max_length=20)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=8)
    #entry_date = models.DateField(blank=False, null=False)
    #exit_date = models.DateField(blank=False, null=False)
    #no_of_events = models.IntegerField(null=False, blank=False)
    #campus_entry = models.BooleanField(default=False)
    #event_entry = models.BooleanField(default=False)
    #entry = models.DateTimeField(null=True, blank=True)
    #exit = models.DateTimeField(null=True, blank=True)
    phone_number = models.BigIntegerField(blank=False)
    events = models.JSONField(models.CharField(default=None, max_length=20), default=None)
    #events_verified = models.JSONField(models.BooleanField(default=False), default=None)

    def __str__(self):
        return str(self.name+" "+self.login_id)


class Event(models.Model):
    token = models.CharField(
    default=None, primary_key=True, editable=False, max_length=20)
    name = models.CharField(max_length=200, null=False, blank=False)
    location = models.CharField(max_length=200)
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    no_of_users = models.BigIntegerField(null=False, blank=False)
    users = models.JSONField(models.CharField(
    default=None, max_length=20), default=None)

    def __str__(self):
        return str(self.name)
