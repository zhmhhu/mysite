from django.conf.urls.defaults import patterns,include
#from mysite.views import current_datetime,hours_ahead,hello,ua_display,display_meta
from mysite.books import views

from django.views.generic import list_detail
from mysite.books.models import Publisher



from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('mysite.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'ua_display'),
    (r'^display_meta/$', 'display_meta'),
    (r'^time/$', 'current_datetime'),
    (r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    (r'^hello/$', 'hello'),
    (r'^search-form/$', views.search_form),
    (r'^search/$', views.search),
    (r'^mydata/(?P<month>\w{3})/(?P<day>\d\d)/$', views.my_view),
    (r'^weblog/', include('mysite.blog.urls')),
    (r'^about/$', 'mysite.views.about'),
)

urlpatterns += patterns('mysite.contact.views',
    (r'^contact/$', 'contact'), 
    (r'^context/$', 'mycontext'), 
    (r'^view1/$', 'view_1'), 
    (r'^view2/$', 'view_2'),                  
)

from mysite.books.models import Book
publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name': 'publisher_list_page.html',
    'extra_context': {'book_list': Book.objects.all}
}

urlpatterns += patterns('',
    (r'^publishers/$', list_detail.object_list, publisher_info)
)

# from django.conf import settings
# 
# if settings.DEBUG:
#     urlpatterns += patterns('',
#         (r'^debuginfo/$', views.debug),
#     )