from django.conf import settings
from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^exampleproject/', include('exampleproject.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG:
    urlpatterns += patterns('',
	    (r'^static_media/(?P<path>.*)$', 
	     'django.views.static.serve', { 
	        'document_root': os.path.join(settings.PROJECT_PATH, 'static_media'),
	        'show_indexes': True }),
    )