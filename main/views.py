from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
# Create your views here.
def home(request):
    return render_to_response('home.html',context_instance=RequestContext(request))