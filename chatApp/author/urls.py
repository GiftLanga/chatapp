from author import views
from django.urls import path

urlpatterns = [
  path('', views.index)
]