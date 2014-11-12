from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^(\d\d\d\d)/$', 'mysite.blog.views.year_detail'),
    #(r'^(\d\d\d\d)/(\d\d)/$', 'mysite.blog.views.month_detail'),
    (r'^(?P<year>\d{1,4})/(?P<month>\d{1,2})/$', 'mysite.blog.views.month_detail'),
    #(r'^(?P<year>\d\d\d\d)/(?P<month>\d\d)/$', 'mysite.blog.views.month_detail'),
)