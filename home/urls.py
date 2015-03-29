from django.conf.urls import patterns
from django.contrib import admin

import settings


admin.autodiscover()

urlpatterns = patterns('',


                       (r'^menu/$', 'user.views.menu'),
                       (r'^search/$', 'user.views.search'),
                       (r'^createRecipeType/$', 'recipe.views.create'),
                       (r'^deleteRecipeType/$', 'recipe.views.delete'),
                       (r'^updateRecipeType/$', 'recipe.views.update'),


                       (r'css/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT + 'css'}),

                       (r'js/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT + 'js'}),
                       (r'^login/$', 'user.views.login'),
                       )
