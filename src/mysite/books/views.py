# Create your views here.
from django.shortcuts import HttpResponse,render_to_response
from mysite.books.models import Book

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET :
        q=request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
            {'books': books, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})
def search_old(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message) 

def debug(request):
    return HttpResponse("It's debug information!")

def my_view(request, month, day):
    return render_to_response('mydata.html',locals())

