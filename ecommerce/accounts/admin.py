from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class UserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'uid', 'username',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telephoneNumber', 'levelUser', 'terms', 'privacy', 'newsletter')}),
    )

admin.site.register(User,UserAdmin)

class AddressesAdmin(admin.ModelAdmin):
    model = Addresses
    list_display = ['id', 'idUser', 'recipientName', 'created', 'lastUpdate',]
    
admin.site.register(Addresses,AddressesAdmin)
