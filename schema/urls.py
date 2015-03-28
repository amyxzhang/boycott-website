from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('schema.views',
                       url(r'^$', 'home'),
                       )