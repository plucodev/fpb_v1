from rest_framework import serializers
from django.db import models
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User


# Create your models here. 
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()
        
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Contact, through='Membership')

    def __str__(self):
        return self.name
        
class Membership(models.Model):
    person = models.ForeignKey(Contact, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        exclude =()
    
        

        
class Location(models.Model):
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.address
        
        
class Provider(models.Model):
    name = models.CharField(max_length=50)
    location = models.ManyToManyField(Location)
    
    def __str__(self):
        return self.name
    
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude =()
        
class ProviderSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True, many=True)
    class Meta:
        model = Provider
        fields = ('id', 'name', 'location')
        exclude = ()
        
class Procedure(models.Model):
    proc_name = models.CharField(max_length=50)
    provider = models.ManyToManyField(Provider)
    # proc_price = models.ManyToManyField(Provider)
    
    
class ProcedureSerializer(serializers.ModelSerializer):
    
    provider = ProviderSerializer(read_only=True, many=True)
    # proc_price = ProviderSerializer(read_only=True, many=True)
    class Meta:
        model = Procedure
        fields = ('id', 'proc_name', 'provider')
        exclude = ()
        

    
    

                
        