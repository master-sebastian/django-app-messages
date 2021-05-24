from basic_project.form import ProfileForm
from .form import MessageForm
from django.contrib.auth.decorators import login_required
from .models import Message, Profile
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse, reverse_lazy
from django.views.generic import  ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
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
            return redirect(
                reverse(
                    "users:detail",
                    kwargs={
                        "slug_username":profile.user.username
                    }
                ))
    else:
        form = ProfileForm()
    return render(request, "manager_messages/profiles/update.html", {
                "profile": profile,
                "form": form
    })

class UpdateProfileView(LoginRequiredMixin, UpdateView):

    template_name = "manager_messages/profiles/update.html"
    model = Profile
    fields = ["first_name", "last_name", "bibliography", "picture"]

    def get_object(self):
        return self.request.user.profile
    
    def get_success_url(self):
        username = self.object.user.username
        self.request.user.first_name = self.object.first_name
        self.request.user.last_name = self.object.last_name
        self.request.user.save()
        return reverse('users:detail', kwargs={
            "slug_username": username
        })


@login_required
def createMessage(request):
    if request.method == "POST":
        form  = MessageForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("manager_messages:index")
    else:
        form = MessageForm()
    return render(request, "manager_messages/messages/create.html", {
                "form": form,
                "profile":request.user.profile
    })

class CreateMessageView(LoginRequiredMixin, CreateView):
    template_name = "manager_messages/messages/create.html"
    form_class = MessageForm
    success_url = reverse_lazy('manager_messages:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = self.request.user.profile
        return context

@login_required
def listMessagesV2(request):
    listMessages = Message.objects.all().order_by("-created")#ordenar por mas recientes
    return render(request, 'manager_messages/messages/index.html',{
            "listMessages": listMessages
        })


class MessagesFeedView(LoginRequiredMixin, ListView):
    template_name = "manager_messages/messages/list_index.html"
    model = Message
    ordering = ('-created',)
    paginate_by = 4
    context_object_name = 'messages'