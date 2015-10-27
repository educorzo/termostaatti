# -*- coding: utf-8 -*-
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

@api_view(['GET'])
def check(request):
    content = {'Exito': 'Sus tokens siguen activos'}
    return Response(content)
