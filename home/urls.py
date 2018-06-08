from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^ref', views.ref, name='ref'),
    url(r'^add/server', views.addserver, name='addserver'),
    url(r'^add/$', views.add, name='add'),
    url(r'^servers/$', views.server, name='servers'),
    url(r'^home/$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^', views.nf, name='nf'),
]
