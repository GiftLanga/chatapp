from author import views
from django.urls import path

urlpatterns = [
  path('login/', views.loginUser, name='login'),
  path('register/', views.register, name='register'),
  path('logout/', views.logoutUser, name='logout'),
]