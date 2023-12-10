from .models import *

'''
The exception could be handled with different cases for the following functions:
- createLogSystem
- createUserLogs
'''
def createLogSystem(ip,type,code,message):
    try:
        LogSystem.objects.create(
            ipSystem=ip,
            logType=type,
            logCode=code,
            logMessage=message
        )
        return True
    except Exception as e:
        print(str(e))
        return False

def createUserLogs(ip,user,type,code,message):
    try:
        LogUser.objects.create(
            ipUser=ip,
            idUser=user,
            logType=type,
            logCode=code,
            logMessage=message
        )
        return True
    except Exception as e:
        print(str(e))
        return False