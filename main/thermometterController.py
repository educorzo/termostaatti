# -*- coding: utf-8 -*-
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from main.thermometter import Thermometter
from main.crontabJob import CrontabJob

@api_view(['GET'])
def getTemperature(request):
    thermometter = Thermometter()
    content = {'Temperature': thermometter.getTemp()}
    return Response(content)

@api_view(['POST'])
def setTemperature(request):
    crontabJob = CrontabJob()
    try:
        temperature = request.POST['temperature']
        crontabJob.setTemperature(temperature)
        content = {'Success': 'La caldera comenzara cuando la temperatura sea inferior a '+temperature}
    except MultiValueDictKeyError :
        content={'Error':request}
    return Response(content)
