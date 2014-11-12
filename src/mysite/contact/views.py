# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from mysite.contact.forms import ContactForm
from django.template import loader, RequestContext
from django.template import Template

'''def contact(request):
    errors = []
    if request.method == 'POST':
        print request.POST.get('email')
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if not request.POST.get('email') or '@' not in request.POST.get('email'):
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html',
        {'errors': errors,
         'subject': request.POST.get('subject', ''),
         'message': request.POST.get('message', ''),
         'email': request.POST.get('email', ''),
         }) '''
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render_to_response('contact_form.html', {'form': form})

def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }


def view_1(request):
    # ...
    return render_to_response('template1.html',
        {'message': 'I am view 1.'},
        context_instance=RequestContext(request, processors=[custom_proc]))

def view_2(request):
    # ...
    return render_to_response('template2.html',
        {'message': 'I am the second view.'},
        context_instance=RequestContext(request, processors=[custom_proc]))

''' #以下代码会因返回值为unicode对象而非python字符串而发生错误，未解决
def view_1(request):
    # ...
    t = Template('template1.html')
    c = RequestContext(request, {'message': 'I am view 1.'},
            processors=[custom_proc])
    return t.render(c)

def view_2(request):
    # ...
    t = loader.get_template('template2.html')
    c = RequestContext(request, {'message': 'I am the second view.'},
            processors=[custom_proc])
    return t.render(c)'''

def mycontext(request):
    errors = []
    if 'con' in request.GET :
        context=request.GET['con']
        if not context:
            errors.append('Enter a context term.')
        elif len(context) > 50:
            errors.append('Please enter at most 50 characters.')
        else:
            return render_to_response('contextresult.html',
            { 'context': context})
    return render_to_response('sendcontext.html', {'errors': errors})

