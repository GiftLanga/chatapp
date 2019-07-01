from django.shortcuts import render, redirect
from django.http import HttpResponse
from author.forms import RegistrationForm, LoginForm, UserDetailsForm

def index(request):
  loginForm = LoginForm()
  registrationForm = RegistrationForm()
  my_dict = {
    'registrationForm': registrationForm,
    'userDetailsForm': UserDetailsForm,
    'loginForm': loginForm,
  }
  return render(request, 'home.html', context=my_dict)

def view_404(request, exception):
    return redirect('/')