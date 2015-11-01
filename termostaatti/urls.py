from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'termostaatti.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/','main.views.home',name='home'),
    url(r'^check/','main.boilerController.check'),#GET
    url(r'^encender/','main.boilerController.turnOn'),#GET
    url(r'^apagar/','main.boilerController.turnOff'),#GET
    url(r'^caldera/','main.boilerController.setBoiler'), #POST
    url(r'^temperatura/','main.thermometterController.getTemperature')#GET
)
