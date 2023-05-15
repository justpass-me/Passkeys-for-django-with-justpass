from django.shortcuts import render


def home(request):
    return render(request,'home.html',{'reg':request.session.get('reg')})