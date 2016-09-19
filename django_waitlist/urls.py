from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^waitlist_entries/', include('waitlist.urls', namespace="waitlist_entries")),
    # Examples:
    # url(r'^$', 'old.views.home', name='home'),
    # url(r'^old/', include('old.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    #url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^users/sign_in/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^users/sign_out/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^users/password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^users/password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^users/password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^users/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^users/reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^users/reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)
