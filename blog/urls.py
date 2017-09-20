from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.baseindex),
    url(r'^tienda/$', views.plantillabase),
    url(r'^case/$', views.case_test),
]