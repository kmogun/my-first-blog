from django.conf.urls import include, url
from . import views
from .views import ControlPanelView, LoginView, LogoutView

urlpatterns = [
    '''url(r'^$', views.baseindex),
    url(r'^tienda/$', views.plantillabase),'''
    url(
        regex=(r'^$'),
        view=ControlPanelView.as_view(),
        name="panel-dashboard"),
    url(
        regex=(r'^login/$'),
        view=LoginView.as_view(),
        name="panel-login"),
    url(
        regex=(r'^logout/$'),
        view=LogoutView.as_view(),
        name="panel-logout"),
]