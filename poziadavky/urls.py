from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^zmena_dodavatela_ee/', views.zmena_dodavatela_ee, name='zmena_dodavatela_ee'),
    url(r'^detail_poziadavky/(?P<pk>[0-9]+)/$', views.detail_poziadavky, name='detail_poziadavky'),
    url(r'^$', views.poziadavky, name='poziadavky'),
]
