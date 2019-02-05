from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from api import views

schema_view = get_schema_view(title='Pastebin API')
urlpatterns = [
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    path('providers/<int:provider_id>', views.ProvidersView.as_view(), name='id-providers'),
    path('providers/', views.ProvidersView.as_view(), name='all-providers'),
    path('procedures/<int:procedure_id>', views.ProceduresView.as_view(), name='id-procedures'),
    path('procedures/', views.ProceduresView.as_view(), name='all-procedures'),
    path('memberships/<int:membership_id>', views.MembershipsView.as_view(), name='id-memberships'),
    path('memberships/', views.MembershipsView.as_view(), name='all-memberships'),
    
]
