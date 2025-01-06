from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador --> Acciones (Metodos)
# MVT = Modelo Template Vista    --. Acciones (Metodos)

def hola_mundo(request):
    return HttpResponse("Hola mundo con Django")