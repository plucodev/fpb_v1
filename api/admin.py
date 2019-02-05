from django.contrib import admin
from api.models import Contact, Provider, Procedure, Location, Group, Membership
# Register your models here.
admin.site.register(Contact)
admin.site.register(Provider)
admin.site.register(Procedure)
admin.site.register(Location)
admin.site.register(Group)
admin.site.register(Membership)
