# -*- coding: utf-8 -*-
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from main.thermometter import Thermometter

@api_view(['GET'])
def getTemperature(request):
    thermometter = Thermometter()
    content = {'Temperature': thermometter.getTemp()}
    return Response(content)
