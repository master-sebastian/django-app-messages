from basic_project.form import ProfileForm
from .form import MessageForm
from django.contrib.auth.decorators import login_required
from .models import Message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core import serializers
import json

LIST_MESSAGES = [
    {
        'message': 'Este es un mensaje de la persona 1'
    },{
        'message': 'Este es un mensaje de la persona 2'
    },{
        'message': 'Este es un mensaje de la persona 3'
    },{
        'message': 'Este es un mensaje de la persona 4'
    },{
        'message': 'Este es un mensaje de la persona 5'
    },{
        'message': 'Este es un mensaje de la persona 6'
    },{
        'message': 'Este es un mensaje de la persona 7'
    }
]

@login_required
def listMessagesV1(request):
    messages = [
        """
            <p>"{message}"</p>
        """.format(**item)
        for item in LIST_MESSAGES
    ]
    return HttpResponse("<br>".join(messages), status=200)

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

@login_required
def updateProfile(request):
    profile = request.user.profile
    if request.method == "POST":
        form  = ProfileForm(request.POST, request.FILES)
        if(form.is_valid()):
            data = form.cleaned_data

            profile.first_name = data["first_name"]
            profile.last_name = data["last_name"]
            profile.bibliography = data["bibliography"]
            profile.birthdate = data["birthdate"]
            if(data["picture"] != None):
                profile.picture = data["picture"]
            profile.save()

            request.user.first_name = profile.first_name
            request.user.last_name = profile.last_name
            request.user.save()
            return redirect("update_profile")
    else:
        form = ProfileForm()
    return render(request, "manager_messages/profiles/update.html", {
                "profile": profile,
                "form": form
    })

@login_required
def createMessage(request):
    if request.method == "POST":
        form  = MessageForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("index")
    else:
        form = MessageForm()
    return render(request, "manager_messages/messages/create.html", {
                "form": form,
                "profile":request.user.profile
    })

@login_required
def listMessagesV2(request):
    listMessages = Message.objects.all().order_by("-created")#ordenar por mas recientes
    return render(request, 'manager_messages/messages/index.html',{
            "listMessages": listMessages
        })