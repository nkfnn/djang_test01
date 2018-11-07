
from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^login_ajax$', views.login_ajax),
    url(r'^login_ajax_check$', views.login_ajax_check),
    url(r'^login1$', views.login1),
    url(r'^login1_check$', views.login1_check),
    url(r'^change_pwd$', views.change_pwd),
    url(r'^verify_code$', views.verify_code),
]
