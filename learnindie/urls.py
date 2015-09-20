from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
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
          
    (r'^accounts/login/$', auth_views.login), #used to have url in front.  I think auth_views is a magical built in view.  
    (r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}), #goes back to home page
    (r'^accounts/register/$', 'mchlrn.views.register'),                   

    (r'^mchlrn/getquestion/$', 'mchlrn.views.get_question'),

    (r'^mchlrn/diagnostic/$', 'mchlrn.views.diagnostic'),
    (r'^mchlrn/diagnostic_complete/$', 'mchlrn.views.diagnostic_complete'),
)
