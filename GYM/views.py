from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#request>response. request handler

def holi(request,edadActual,anio):
    #edadActual=28
    periodo=anio-2022
    edadFutura=edadActual+periodo

    name="hohohohoho"
    doc="""
    <html>
    <body>
    <h1>en el año %s tendrás %s años</h1>
    </body>
    </html>
    """ %(anio,edadFutura)
    return HttpResponse(doc) 