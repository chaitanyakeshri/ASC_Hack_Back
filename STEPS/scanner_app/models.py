from django.db import models
from django import forms
# Create your models here.
class Scanner(models.Model):
    login_id=models.CharField(primary_key=True,max_length=10)
    password=models.CharField(max_length=8)
    location=models.CharField(max_length=50)
    entry_check= models.BooleanField(default=False)
    event_check=models.BooleanField(default= not entry_check)
    gate_number=models.IntegerField(default=1)
    event=models.CharField(max_length=200,null=False, blank=False)

    def __str__(self):
        return str(self.event+" "+str(self.gate_number))
    
class Event(models.Model):
    token=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200, null=False, blank=False)
    location=models.CharField(max_length=200)
    date=models.DateField(null=False)
    time=models.TimeField(null=False)
    no_of_users=models.BigIntegerField(null=False,blank=False)
    users=models.JSONField()
    
    def __str__(self):
        return str(self.name)
   

class User(models.Model):
    login_id=models.CharField(max_length= 20,primary_key=True)
    name= models.CharField(max_length=200)
    password=forms.CharField(min_length=8)
    #entry_date=models.DateField(blank=False,null=False)
    #exit_date=models.DateField(blank=False,null=False)
   # no_of_events=models.IntegerField(null=False, blank=False)
   # campus_entry= models.BooleanField(default=False)
   # event_entry=models.BooleanField(default=False)
   # entry=models.DateTimeField(null=True, blank=True)
   # exit_f = models.DateTimeField(null=True, blank=True)
    phone_number=models.BigIntegerField(blank=False)
    events = models.CharField(default=None,max_length=200)
   # events_verified=models.JSONField(models.BooleanField(default=False), default=None)

    def __str__(self):
        return str(self.name+" "+self.login_id)