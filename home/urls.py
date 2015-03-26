from django.conf.urls import patterns
import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',


                       (r'^menu/$', 'user.views.menu'),
                       (r'^search/$', 'user.views.search'),
                       (r'^createRecipeType/$', 'recipeType.views.create'),
                       (r'^deleteRecipeType/$', 'recipeType.views.delete'),
                       (r'^updateRecipeType/$', 'recipeType.views.update'),


                       (r'css/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT + 'css'}),

                       (r'js/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT + 'js'}),
                       (r'^login/$', 'user.views.login'),
                       )
