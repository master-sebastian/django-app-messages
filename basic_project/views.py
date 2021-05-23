
#utilities django
from django.http import HttpResponse
#utilities python
from datetime import datetime as clock
import json

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

def getMessageIndexV3(request):
    """return list ids ordered"""
    if(request.GET.get("list_ids") == None ):
        return HttpResponse(json.dumps({
                "status": "error",
                "message": "No hay ninguna lista de ids en este request"
                }, indent=4), content_type="application/json", status=422)
    try:
        listIds = [ float(_id) for _id in request.GET["list_ids"].split(",")]

    except:
        return HttpResponse(json.dumps({
                "status": "error",
                "message": "La lista que envio no posible usarla verifique que sean de solo numeros"
            }, indent=4), content_type="application/json", status=422)
        
    return HttpResponse(json.dumps({
            "status": "success",
            "message": "Se recibio la lista de ids y se ordeno",
            "list_ids": sorted(listIds)
        }, indent=4), content_type="application/json", status=200)

def getMessageIndexV4(request, name, age):
    """return message of happy birthday"""
    if(request.GET.get("subject") == None ):
        return HttpResponse(json.dumps({
                "status": "error",
                "message": "El asunto es requerido para generar el mensaje en este request"
                }, indent=4), content_type="application/json", status=422)
    if(age < 0):
         return HttpResponse(json.dumps({
                "status": "error",
                "message": "La edad no puede ser negativa"
                }, indent=4), content_type="application/json", status=422)
    return HttpResponse(json.dumps({
            "status": "success",
            "message": "{text_subject} : Feliz dia {text_name} por cumpir {text_age} {text_age2}".format(text_name=name, text_age=age, text_subject=request.GET["subject"], text_age2= ("años", "año")[age == 1] )
        }, indent=4), content_type="application/json", status=200)

def createUserAdminDefault(request):
    from django.contrib.auth.models import User
    userName = "super-admin"
    if len(User.objects.filter(username=userName)) > 0:
        return HttpResponse(json.dumps({
            "status": "success",
            "message": "Ya esta creado el usuario por defecto"
        }, indent=4), content_type="application/json", status=200)   
    User.objects.create_user(
        username=userName, 
        is_superuser=1,
        password="admin4334",
        is_staff=1
    )
    return HttpResponse(json.dumps({
            "status": "success",
            "message": "Se creo el usuario por defecto"
        }, indent=4), content_type="application/json", status=200)