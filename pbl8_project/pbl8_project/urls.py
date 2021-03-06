from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from pbl.views import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^treatments/(?P<slug>[\w-]+)/$', 'pbl.views.view_treatment'),
    url(r'^treatments/comments/', include('fluent_comments.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', 'pbl.views.home'),

    # Examples:
    # url(r'^$', 'pbl8_project.views.home', name='home'),
    # url(r'^pbl8_project/', include('pbl8_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
