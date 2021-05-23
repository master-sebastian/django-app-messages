from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.

def loginApp(request):    
    if request.method == "POST":
        nextPOST = request.POST.get("next")
        if(request.POST.get("username") == None):
            return render(request, "users/login.html", {
                "error_message": "No existe la key 'username' en el request "
            })
        if(request.POST.get("password") == None):
            return render(request, "users/login.html", {
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
            return render(request, "users/login.html", {
                "error_message": "El usuario o la contraseña son incorrectos"
            })
    elif request.method == "GET":
        nextGET = request.GET.get("next")
        return render(request, "users/login.html", {
            "next": nextGET
        })
    return HttpResponse("", stauts=404)

def logoutApp(request):
    logout(request)
    return redirect("login")