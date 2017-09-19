# views.py
from django.shortcuts import render
#  from django.views.generic import FormView, TemplateView, RedirectView


# Create your views here.

def baseindex(request):
    return render(request, 'blog/baseindex.html', {})

def plantillabase(request):
    return render(request, 'blog/plantilla_base.html', {})


