from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learnindie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'mchlrn.views.home'),
    (r'^mchlrn/parsePDF/$', 'mchlrn.views.parse_PDF'),
    (r'^mchlrn/questionoftheday/$', 'mchlrn.views.question_of_the_day'),
    (r'^mchlrn/qotdbatch/$', 'mchlrn.views.qotd_batch'), 

    (r'^mchlrn/batch4tests/$', 'mchlrn.views.batch_4tests'), 

    (r'^mchlrn/getquestion/$', 'mchlrn.views.get_question')
)
