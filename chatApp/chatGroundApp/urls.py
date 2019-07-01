from . import views
from django.urls import path

urlpatterns = [
  path('', views.chatGroundHome, name='chatGround')
]