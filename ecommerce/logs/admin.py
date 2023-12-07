from django.contrib import admin
from .models import *
# Register your models here.

class LogUserAdmin(admin.ModelAdmin):
    model = LogUser
    list_display = ['id', 'created', 'ipUser', 'idUser', 'logType', 'logCode', 'logMessage']
    
admin.site.register(LogUser,LogUserAdmin)

