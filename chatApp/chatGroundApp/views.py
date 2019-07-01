from django.shortcuts import render, redirect

# Create your views here.
def chatGroundHome(request):
  if request.user.is_authenticated:
    my_dict = {
      "username": request.user.username
    }
    return render(request, 'chatGround/chatGround.html', context=my_dict)
  else:
    return redirect('/')
