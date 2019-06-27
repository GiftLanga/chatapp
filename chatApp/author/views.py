from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  my_dict = {'component':'<h1> THe component </h1>'}
  return render(request, 'index.html', context=my_dict)
