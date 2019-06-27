from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
  my_dict = {'component':'<h1> THe component </h1>', 'loggedin': False}
  return render(request, 'index.html', context=my_dict)

def view_404(request, exception):
    return redirect('/')