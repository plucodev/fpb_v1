from django.shortcuts import render
import json
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Contact, ContactSerializer, Provider, ProviderSerializer, Procedure, ProcedureSerializer, Membership, MembershipSerializer



@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactsView(APIView):
    def get(self, request, contact_id=None):

        if contact_id is not None:
            contact = Contact.objects.get(id=contact_id)
            serializer = ContactSerializer(contact, many=False)
            return Response(serializer.data)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, contact_id):
        
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ProvidersView(APIView):
    def get(self, request, provider_id=None):

        if provider_id is not None:
            provider = Provider.objects.get(id=provider_id)
            serializer = ProviderSerializer(provider, many=False)
            return Response(serializer.data)
        else:
            providers = Provider.objects.all()
            serializer = ProviderSerializer(providers, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, provider_id):
        
        provider = Provider.objects.get(id=provider_id)
        provider.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)        
        
        
class MembershipsView(APIView):
    def get(self, request, membership_id=None):

        if membership_id is not None:
            membership = Membership.objects.get(id=membership_id)
            serializer = MembershipSerializer(membership, many=False)
            return Response(serializer.data)
        else:
            memberships = Membership.objects.all()
            serializer = MembershipSerializer(memberships, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, membership_id):
        
        membership = Membership.objects.get(id=membership_id)
        membership.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)  
        
class ProceduresView(APIView):
    def get(self, request, procedure_id=None):

        if procedure_id is not None:
            procedure = Procedure.objects.get(id=procedure_id)
            serializer = ProcedureSerializer(procedure, many=False)
            return Response(serializer.data)
        else:
            procedures = Procedure.objects.all()
            serializer = ProcedureSerializer(procedures, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = ProcedureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, procedure_id):
        
        procedure = Procedure.objects.get(id=procedure_id)
        procedure.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)  