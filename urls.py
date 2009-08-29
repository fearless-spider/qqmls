import os
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

site_media = os.path.join(
        os.path.dirname(__file__), 'site_media'
    )

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout'),
    (r'^reset/$', 'django.contrib.auth.views.password_reset'),
    (r'^change/$', 'django.contrib.auth.views.password_change'),
    # i18n
    (r'^i18n/', include('django.conf.urls.i18n')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media}),
)
