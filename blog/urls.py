from django.conf.urls import include, url
from . import views
from .views import ControlPanelView, LoginView, LogoutView

urlpatterns = [
    #url(r'^$', views.baseindex),
    #url(r'^tienda/$', views.plantillabase),
    url(r'^$', ControlPanelView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
]