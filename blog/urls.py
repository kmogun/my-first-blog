from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.baseindex),
    url(r'^tienda/$', views.plantillabase),
    url(r'^tienda/case/$', views.case_test, name='case_test'),
    url(r'^list/$', views.PersonaList.as_view(), name='plist'),
    url(r'^add/$', views.add_persona, name='padd'),
]