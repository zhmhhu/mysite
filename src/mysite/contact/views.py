# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from mysite.contact.forms import ContactForm
from django.template import loader, RequestContext
from django.template import Template


from django.shortcuts import HttpResponse,render_to_response


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


#cookies test
def show_color(request):
    if "favorite_color" in request.COOKIES:
        return HttpResponse("Your favorite color is %s" %request.COOKIES["favorite_color"])
    else:
        #return HttpResponse("You don't have a favorite color.")
        return render_to_response('color_form.html')
    
#如果request没有数据，则显示cookies数据，每一次request提交，则写一次cookies
def set_color(request):
    if "favorite_color" in request.GET:
        favorite_color=request.GET['favorite_color']
        # Create an HttpResponse object...
        response = HttpResponse("Your favorite color is now %s" %request.GET["favorite_color"])
        # ... and set a cookie on the response
        response.set_cookie("favorite_color",
                            request.GET["favorite_color"])
        #return response
        return render_to_response('color_form.html',{ 'favorite_color': favorite_color})
    elif"favorite_color" in request.COOKIES:
        #return HttpResponse("Your favorite color is %s" %request.COOKIES["favorite_color"]) 
        return render_to_response('color_form.html', {'favorite_color': request.COOKIES["favorite_color"]})     
    else:
        #return HttpResponse("You didn't give a favorite color.")
        return render_to_response('color_form.html')

#session test

from django.http import Http404
def post_comment(request,comments):    #加入了参数，原书中没有
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')

    if 'comment' not in request.POST:
        raise Http404('Comment not submitted')

    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")

    c = comments.Comment(comment=request.POST['comment'])
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')


#login test
def login(request,Member):     #加入了参数，原书中没有
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        m = Member.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponseRedirect('/you-are-logged-in/')
    except Member.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")
    if request.method == 'POST':

        # Check that the test cookie worked (we set it below):
        if request.session.test_cookie_worked():

            # The test cookie worked, so delete it.
            request.session.delete_test_cookie()

            # In practice, we'd need some logic to check username/password
            # here, but since this is an example...
            try:
                m = Member.objects.get(username=request.POST['username'])
                if m.password == request.POST['password']:
                    request.session['member_id'] = m.id
                    return HttpResponseRedirect('/you-are-logged-in/')
            except Member.DoesNotExist:
                    return HttpResponse("Your username and password didn't match.")
            return HttpResponse("You're logged in.")

        # The test cookie failed, so display an error message. If this
        # were a real site, we'd want to display a friendlier message.
        else:
            return HttpResponse("Please enable cookies and try again.")

    # If we didn't post, send the test cookie along with the login form.
    request.session.set_test_cookie()
    return render_to_response('foo/login_form.html')
    
#login out test    
def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")