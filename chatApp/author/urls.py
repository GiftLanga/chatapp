from author import views
from django.urls import path

urlpatterns = [
  path('login/', views.authenticate, name='login'),
  path('register/', views.register, name='register'),
]