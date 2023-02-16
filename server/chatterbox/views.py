from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from gateway.rasa import Rasa

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@require_http_methods(["GET"])
def say(request):
    message = request.GET.get('message')
    response = Rasa().say(message)
    return JsonResponse(response, safe=False)