from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^failing/', views.failing, name='failing'),
    url(r'^(?P<question_id>.*)/$', views.detail, name='detail'),
]
