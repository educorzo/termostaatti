# -*- coding: utf-8 -*-
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.utils.datastructures import MultiValueDictKeyError
from main.remoteBoiler import Boiler

@api_view(['GET'])
def check(request):
    caldera = Boiler()
    content = caldera.getState()
    return Response(content)

@api_view(['GET'])
def turnOn(request):
    caldera = Boiler()
    content = caldera.turnOn()
    return Response(content)

@api_view(['GET'])
def turnOff(request):
    caldera = Boiler()
    content = caldera.turnOff()
    return Response(content)

@api_view(['POST'])
def setBoiler(request):
    caldera = Boiler()
    try:
        if request.POST['state']=='on' :
            content = caldera.turnOn()
        elif request.POST['state']=='off' :
            content = caldera.turnOff()
        else:
            content = {'state': 'Format not recognized'}
    except MultiValueDictKeyError :
        content={'state':request}
    return Response(content)


