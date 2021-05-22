#utilities django
from django.http import HttpResponse
#utilities python
from datetime import datetime as clock
def getMessageIndexV1(request):
    """return a message"""
    currentDateTime = clock.now().strftime("%b %dth %Y - %H:%M hrs")
    return HttpResponse("Este es el index bienvenido sea siendo {textDateTime}".format(
        textDateTime = currentDateTime))

def getMessageIndexV2(request):
    """return a message"""
    import pdb
    pdb.set_trace()
    #el caracter c y enter para salir del pdb
    #Nota:  si en algun momento quiere usar en una sola linea varias instrucciones use ;
    return HttpResponse('Saludos a todos')
