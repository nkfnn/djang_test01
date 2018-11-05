
from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^login_ajax$', views.login_ajax),
    url(r'^login_ajax_check$', views.login_ajax_check)
]
