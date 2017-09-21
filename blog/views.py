# views.py
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .forms import RegistroUsuarios
from .models import PersonaForm
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

def add_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            new_persona = form.save()

            return HttpResponseRedirect(reverse('upersona:plist'))
