from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('say', views.say, name='say'),
]