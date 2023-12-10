from django.contrib import admin
from .models import *
# Register your models here.

class LogUserAdmin(admin.ModelAdmin):
    model = LogUser
    list_display = ['id', 'created', 'ipUser', 'idUser', 'logType', 'logCode', 'logMessage']
    
admin.site.register(LogUser,LogUserAdmin)

class LogSystemAdmin(admin.ModelAdmin):
    model = LogSystem
    list_display = ['id', 'created', 'ipSystem', 'logType', 'logCode', 'logMessage']
    
admin.site.register(LogSystem,LogSystemAdmin)

