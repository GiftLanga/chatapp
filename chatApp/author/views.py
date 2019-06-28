from django.shortcuts import render, redirect
from django.http import HttpResponse
from author import models

def authenticate(request):
  if(request.method == "POST"):
    form  = request.POST.dict()
    username = form.get("username")
    password = form.get("password")
    return render(request, 'chatGround/chatGround.html', context=None)#redirect
  else:
    return redirect('/')
