from django.http import HttpResponse
from django.shortcuts import render

# Create your views here


def home(request, template="home.html"):
    return render(request, template)

def login2(request, template="login2.html"):
    return render(request, template)

def manual(request, template="manual.html"):
    return render(request, template)

def materia(request, template="materia.html"):
    return render(request, template)

def notificaciones(request, template="notificaciones.html"):
    return render(request, template)

def contact(request, template="contact.html"):
    return render(request, template)

def soporte(request, template="soporte.html"):
    return render(request, template)


