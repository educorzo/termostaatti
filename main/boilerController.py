# -*- coding: utf-8 -*-
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from main.boiler import boiler

@api_view(['GET'])
def check(request):
    content = {'Success': 'Todo va bien!'}
    return Response(content)

@api_view(['GET'])
def turnOn(request):
    caldera = boiler()
    caldera.turnOn()
    content = {'Success': 'Todo va bien!'}
    return Response(content)