# views.py
from django.shortcuts import render
from .forms import RegistroUsuarios
from django.views.generic import FormView, TemplateView, RedirectView


# Create your views here.

def baseindex(request):
    form = FormView(RegistroUsuarios)
    print(form)
    return render(request, 'blog/prueba.html', {'el_form': form})

def plantillabase(request):
    return render(request, 'blog/plantilla_base.html', {})

def case_test(request):
    return render(request, 'blog/case.html', {})


