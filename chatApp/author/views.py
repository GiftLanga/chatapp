from django.shortcuts import render, redirect
from django.http import HttpResponse
from author.forms import LoginForm, RegistrationForm, UserDetailsForm

def authenticate(request):
  if(request.method == "POST"):
    form  = request.POST.dict()
    username = form.get("username")
    password = form.get("password")
    return render(request, 'chatGround/chatGround.html', context=None)#redirect
  else:
    return redirect('/')

def register(request):
  if request.method == "POST":
    print("posting")
    user_details_form = UserDetailsForm(data=request.POST)
    registration_form = RegistrationForm(data=request.POST)

    if user_details_form.is_valid() and registration_form.is_valid():
      print("valid")
      user  = user_details_form.save()
      user.set_password(user.password)
      user.save()

      register = registration_form.save(commit=False)
      register.user = user
      register.save()
      return authenticate(request)
    else:
      my_dict = {
        'registrationForm': registration_form,
        'userDetailsForm': user_details_form,
        'loginForm': LoginForm(),
      }
      print(user_details_form.errors, registration_form.errors)
      return render(request, 'home.html', context=my_dict)
  else:
    return redirect('/')
