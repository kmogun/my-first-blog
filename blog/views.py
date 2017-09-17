# views.py
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, RedirectView

# imports de autenticación
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy, reverse

# Create your views here.

def baseindex(request):
    return render(request, 'blog/baseindex.html', {})

def plantillabase(request):
    return render(request, 'blog/plantilla_base.html', {})

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "blog/login.html"
    success_url = reverse_lazy("blog/baseindex.html")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

class LogoutView(RedirectView):
    pattern_name = 'panel_login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('panel-login'))
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class ControlPanelView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/login.html'

    def get_context_data(self, **kwargs):
        context = super(ControlPanelView, self).get_context_data(**kwargs)
        return context



