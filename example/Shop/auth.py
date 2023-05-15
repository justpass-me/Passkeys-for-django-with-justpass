from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import User

def loginView(request):
    context={}
    if request.method=="POST":
        mobile=request.POST["mobile"]
        u = User.objects.filter(phone_number=mobile)
        if u.exists():
            user = u[0]
            request.session["username"] = user.username
            if user.mfa_enabled:
                request.session["token"] = user.phone_number
                request.session["OP_MODE"] = "LOGIN"
                return redirect('oidc_authentication_init')
            else:
                return redirect('otp')
        context["invalid"]=True
    return render(request, "login.html", context)

def otp(request):
    context={}
    if request.method == "POST":
        otp = request.POST["otp"]
        if otp == "5432":
            return create_session(request, request.session["username"])
        context["invalid"] = True
    return render(request,'otp.html',context)



def create_session(request,username=None,user=None):
    if user is None and username:
        user=User.objects.get(username=username)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
    elif user is None and username is None:
        raise Exception("Invalid Parameters")
    login(request, user)
    if not request.user.mfa_enabled:
        return redirect('enroll_justpass')
    return HttpResponseRedirect(reverse('home'))


def mfa(request):
    return render(request,"mfa.html",{})


def logoutView(request):
    logout(request)
    return render(request,"logout.html",{})

def reset(request):
    for user in User.objects.all():
        user.mfa_enabled =0
        user.token = None
        user.save()
    return HttpResponse("Demo Reset Successfully")
