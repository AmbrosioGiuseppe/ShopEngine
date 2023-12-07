from django.db import models
from accounts.models import User
# Create your models here.

EVENT_TYPE = [
    ('INFO', 'INFO'),
    ('DANGER', 'DANGER'),
    ('REQUEST', 'REQUEST')
]

class LogUser(models.Model):
    created         = models.DateTimeField(auto_now_add=True)
    ipUser          = models.CharField(max_length=100)
    idUser          = models.ForeignKey(User,on_delete=models.CASCADE)
    logType         = models.CharField(max_length=255,choices=EVENT_TYPE,blank=True)
    logCode         = models.IntegerField(blank=True)
    logMessage      = models.TextField()
    
    def __str__(self):
        return str(self.idUser)
    
    
