from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def ofertas(request):
    return render(request, 'ofertas.html')

def contacto(request):
    return render(request, 'contacto.html')

