from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^waitlist_entries/', include('waitlist.urls', namespace="waitlist_entries")),
    # Examples:
    # url(r'^$', 'old.views.home', name='home'),
    # url(r'^old/', include('old.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
