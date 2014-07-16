from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learnindie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^admin/', include(admin.site.urls)),

    (r'^$', 'machlearn.views.home'),
    (r'^machlearn/parsePDF/$', 'machlearn.views.parse_PDF'),
)
