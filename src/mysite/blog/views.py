from django.shortcuts import render_to_response

def year_detail(request,year):
    return render_to_response('year_detail.html',locals())

def month_detail(request,month,year):
    return render_to_response('month_detail.html',locals())