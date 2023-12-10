

##Find Public IP
def findPublicIP(request):
    try:
        public_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
    except:
        public_ip = 'IP Not found'
    
    return public_ip