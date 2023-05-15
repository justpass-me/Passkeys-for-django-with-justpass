from django.http import JsonResponse
from django.shortcuts import redirect, render


def auth_success(request):
    platform = request.session.get("AMWALPLATFORM")
    if platform == "app":
        return JsonResponse({
            "username": request.user.username,
            "token": request.session.session_key
        })
    return redirect('home')

def auth_failure(request):
    platform = request.session.get("AMWALPLATFORM")
    if platform == "app":
        return JsonResponse({"err":"Failed"})

    return render(request, 'login.html', {"failed": True})

def reg_success(request):
    request.user.mfa_enabled = True
    request.user.save()
    request.session["reg"] = True
    return redirect('home')

def reg_failure(request):
    request.session["reg"] = False
    return redirect('home')