from django.conf.urls import patterns, include, url
from proj1.views import hello, start, testread

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj1.views.home', name='home'),
    # url(r'^proj1/', include('proj1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^hello/$', hello),
    url(r'^stinky/$', start),
    url(r'^test/$', testread),
)
