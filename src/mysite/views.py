'''
Created on 2014-10-16

@author: Lenovo
'''
# from django.template.loader import get_template
# from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def hours_ahead(request, offset):
    #offset = int(offset)
    #dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    #return HttpResponse(html)
    hour_offset = int(offset)
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render_to_response('hours_ahead.html', locals())

def current_datetime(request):
    #now = datetime.datetime.now()
    #return render_to_response('current_datetime.html', {'current_date': now})
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())

def hello(request):
    return HttpResponse("Hello world")

def ua_display(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Your browser is %s" % ua)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr><td>next</td>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
