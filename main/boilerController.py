# -*- coding: utf-8 -*-
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from main.boiler import Boiler

@api_view(['GET'])
def check(request):
    content = {'Success': 'Todo va bien!'}
    return Response(content)

@api_view(['GET'])
def turnOn(request):
    caldera = Boiler()
    caldera.turnOn()
    content = {'Success': 'Caldera encendida!'}
    return Response(content)

@api_view(['GET'])
def turnOff(request):
    caldera = Boiler()
    caldera.turnOff()
    content = {'Success': 'Caldera apagada!'}
    return Response(content)

@api_view(['POST'])
def setBoiler(request):
    caldera = Boiler()
    try:
        if request.POST['state']=='on' :
            caldera.turnOn()
            content = {'Success': 'Caldera encendida!'}
        elif request.POST['state']=='off' :
            caldera.turnOff()
            content = {'Success': 'Caldera apagada!'}
        else:
            content = {'Error': 'Formato no reconocido'}
    except MultiValueDictKeyError :
        content={'Error':'Algo ha ido mal!'}
    return Response(content)

