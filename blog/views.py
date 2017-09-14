from django.shortcuts import render

# Create your views here.

def baseindex(request):
    return render(request, 'templates/baseindex.html',)