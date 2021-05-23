from django.db.models import base
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from manager_messages.models import Profile
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
            return redirect("index")
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
    return redirect("login")

def signupApp(request):
    baseTemplate = "users/signup.html"
    if request.method == "POST":
        if(request.POST.get("first_name") == None):
            return render(request, baseTemplate, {
                "error_message": "No existe la key 'first_name' en el request"
            })
        if(request.POST.get("last_name") == None):
            return render(request, baseTemplate, {
                "error_message": "No existe la key 'last_name' en el request"
            })
        if(request.POST.get("username") == None):
            return render(request, baseTemplate, {
                "error_message": "No existe la key 'username' en el request "
            })
        if(request.POST.get("password") == None):
            return render(request, baseTemplate, {
                "error_message": "No existe la key 'password' en el request"
            })
        if(request.POST.get("password_confirmation") == None):
            return render(request, baseTemplate, {
                "error_message": "No existe la key 'password_confirmation' en el request"
            })
        if(request.POST.get("email") == None):
            return render(request, baseTemplate, {
                "error_message": "No existe la key 'email' en el request"
            })
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]
        password_confirmation = request.POST["password_confirmation"]
        email = request.POST["email"]
        
        if password != password_confirmation:
            return render(request, baseTemplate, {
                "error_message": "La contraseña y la confirmación de la contraseña tienen que ser iguales"
            })

        try:
            user = User.objects.create_user(username=username, password=password)
        except:
            return render(request, baseTemplate, {
                "error_message": "Error al registrar el usuario intentelo nuevamente ...👍"
            })

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        profile = Profile(user=user)
        profile.first_name = user.first_name
        profile.last_name = user.last_name
        profile.role_id = 4
        profile.save()

        return redirect("login")

    elif request.method == "GET":
        return render(request, baseTemplate)
    return HttpResponse("", stauts=404)
