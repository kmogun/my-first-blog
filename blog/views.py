# views.py
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, RedirectView

# imports de autenticación
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy, reverse

# Create your views here.

#'''def baseindex(request):
#    return render(request, 'blog/baseindex.html', {})'''

#'''def plantillabase(request):
#    return render(request, 'blog/plantilla_base.html', {})'''

class LoginView(FormView):
    form_class = AuthenticationForm()
    template_name = "plantilla_base.html"
    success_url = reverse_lazy("blog/plantilla_base.html")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

