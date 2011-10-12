from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^person/$', 'sna.person.views.index' ),
    (r'^person/graph$', 'sna.person.views.statistics'),
    (r'^person/export.ucinet$', 'sna.person.views.export'),
    (r'^person/(?P<id>\d+)/$', 'sna.person.views.show'),
    (r'^person/(?P<id>\d+)/entry$', 'sna.person.views.data'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$' , 'sna.person.views.index' ),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
