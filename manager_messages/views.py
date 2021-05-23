from django.contrib.auth.decorators import login_required
from manager_messages.models import Message
from manager_messages.models import Profile
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core import serializers
import json

LIST_MESSAGES = [
    {
        'author_name': 'Persona 1',
        'message': 'Este es un mensaje de la persona 1'
    },{
        'author_name': 'Persona 2',
        'message': 'Este es un mensaje de la persona 2'
    },{
        'author_name': 'Persona 3',
        'message': 'Este es un mensaje de la persona 3'
    },{
        'author_name': 'Persona 4',
        'message': 'Este es un mensaje de la persona 4'
    },{
        'author_name': 'Persona 5',
        'message': 'Este es un mensaje de la persona 5'
    },{
        'author_name': 'Persona 6',
        'message': 'Este es un mensaje de la persona 6'
    },{
        'author_name': 'Persona 7',
        'message': 'Este es un mensaje de la persona 7'
    }
]

@login_required
def listMessagesV1(request):
    messages = [
        """
            <h1>{author_name}</h1>
            <hr>
            <p>"{message}"</p>
        """.format(**item)
        for item in LIST_MESSAGES
    ]
    return HttpResponse("<br>".join(messages), status=200)

def listMessagesV2(request):
    return render(request, 'manager_messages/messages/index.html',{
            "listMessages": LIST_MESSAGES
        })

def runSeederMessages(request):
    ids = []
    for message in LIST_MESSAGES:
        objMessage = Message(**message)
        objMessage.save()
        ids.append(objMessage.pk)
        objMessage = Message.objects.create(**message)
        ids.append(objMessage.pk) 
    return HttpResponse(json.dumps(
        {
            "status": "success",
            "message": "Se generaron messagen por defecto en la app",
            "ids": ids
        }
    , indent=4), content_type="application/json", status=201)

def getListMessagesV1(request):
    return HttpResponse(json.dumps(
        {
            "status": "success",
            "message": "List",
            "list_message": json.loads(
                    serializers.serialize("json", 
                        Message.objects.all()
                    )
                )
        }
    , indent=4), content_type="application/json", status=200)

def getListMessagesByIdV1(request,id):
    return HttpResponse(json.dumps(
        {
            "status": "success",
            "message": "List",
            "list_message": json.loads(
                    serializers.serialize("json", 
                        Message.objects.filter(id = id)
                    )
                )
        }
    , indent=4), content_type="application/json", status=200)


def updateProfile(request):
    from datetime import date
    profile = request.user.profile

    if request.method == "POST":
        data = request.POST
        dateTime = data["birthdate"].split("-")
        dataFile = request.FILES
        profile.first_name = data["first_name"]
        profile.last_name = data["last_name"]
        profile.bibliography = data["bibliography"]

        if(len(dateTime) == 3):
            if(dateTime[0].isnumeric() and dateTime[1].isnumeric() and dateTime[2].isnumeric()):
                profile.birthdate = date(int(dateTime[0]), int(dateTime[1]), int(dateTime[2]))
                
        if dataFile.get("picture") != None:
            profile.picture = dataFile["picture"]
        profile.save()

        request.user.first_name = profile.first_name
        request.user.last_name = profile.last_name
        request.user.save()

        return redirect("update_profile")
    
    return render(request, "manager_messages/profiles/update.html", {
                "profile": profile
    })