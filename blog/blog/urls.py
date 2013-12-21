from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'principal.views.index'),
    url(r'^entrada/(?P<pk>\d+)/$', 'principal.views.entrada'),
    url(r'^poncomentario/(\d+)/$', 'principal.views.poncomentario'),

    url(r'^admin/', include(admin.site.urls)),
)
