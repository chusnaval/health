from django.conf.urls import patterns
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #url(r'^admin/', include(admin.site.urls)),
    (r'^search/$', 'user.views.search'),
    (r'^combo/$', 'user.views.combo'),

    (r'css/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT + 'templates/css'}),

    (r'js/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT  + 'templates/js'}),
)
