from django.conf.urls import patterns, include, url
import schema

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'schema.views.home'),
    url(r'^create$', 'schema.views.create'),
    url(r'^404', 'schema.views.error'),
    url(r'^petition/(?P<petition_id>[\w-]+)/', 'schema.views.petition'),
  
    (r'^accounts/', include('registration.backends.default.urls')),
   #  url(r'^boycott_website/', include('boycott_website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
