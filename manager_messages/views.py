from django.shortcuts import render
from django.http import HttpResponse
import json

LIST_MESSAGES = [
    {
        "author_message": "Persona 1",
        "message": "Este es un mensaje de la persona 1"
    },{
        "author_message": "Persona 2",
        "message": "Este es un mensaje de la persona 2"
    },{
        "author_message": "Persona 3",
        "message": "Este es un mensaje de la persona 3"
    },{
        "author_message": "Persona 4",
        "message": "Este es un mensaje de la persona 4"
    },{
        "author_message": "Persona 5",
        "message": "Este es un mensaje de la persona 5"
    },{
        "author_message": "Persona 6",
        "message": "Este es un mensaje de la persona 6"
    },{
        "author_message": "Persona 7",
        "message": "Este es un mensaje de la persona 7"
    }
]

def listMessagesV1(request):
    messages = [
        """
            <h1>{author_message}</h1>
            <hr>
            <p>"{message}"</p>
        """.format(**item)
        for item in LIST_MESSAGES
    ]
    return HttpResponse("<br>".join(messages), status=200)

def listMessagesV2(request):
    return render(request, 'messages/index.html',{
            "listMessages": LIST_MESSAGES
        })
