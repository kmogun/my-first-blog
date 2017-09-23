# views.py
from django.shortcuts import render


# Create your views here.

def baseindex(request):
    return render(request, 'blog/prueba.html', {})

def plantillabase(request):
    return render(request, 'blog/plantilla_base.html', {})

def case_test(request):
    return render(request, 'blog/case.html', {})

