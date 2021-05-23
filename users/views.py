from django.db.models import base
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .form import SignupForm
# Create your views here.

def loginApp(request):    

    baseTemplate = "users/login.html"

    if request.method == "POST":
        nextPOST = request.POST.get("next")
        if(request.POST.get("username") == None):
            return render(request, baseTemplate, {
                "error_message": "No existe la key 'username' en el request "
            })
        if(request.POST.get("password") == None):
            return render(request, baseTemplate, {
                "error_message": "No existe la key 'password' en el request"
            })
        username = request.POST["username"]
        password = request.POST["password"]
        auth = authenticate(request, username=username, password=password)
        if auth:
            login(request, auth)
            if nextPOST != None:
                return redirect(nextPOST)
            return redirect("manager_messages:index")
        else:
            return render(request, baseTemplate, {
                "error_message": "El usuario o la contraseña son incorrectos"
            })
    elif request.method == "GET":
        nextGET = request.GET.get("next")
        return render(request, baseTemplate, {
            "next": nextGET
        })
    return HttpResponse("", stauts=404)

def logoutApp(request):
    logout(request)
    return redirect("users:login")

def signupApp(request):
    baseTemplate = "users/signup.html"
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
        return render(request, baseTemplate, context={"form":form})
    elif request.method == "GET":
        return render(request, baseTemplate, context={"form":form})
    return HttpResponse("", stauts=404)
