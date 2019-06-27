from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
  my_dict = {'loggedin': False}
  return render(request, 'home.html', context=my_dict)

def view_404(request, exception):
    return redirect('/')