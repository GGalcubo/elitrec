# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Categoria, Producto, Oferta

def index(request):
	productos = Producto.objects.all()
	ofertas = Oferta.objects.all()
	context = {'productos': productos, 'ofertas': ofertas,}
	return render(request, 'index.html', context)

def catalogo(request):
    mensaje = ''
    
    productos = Producto.objects.all()
    context = {'productos': productos,}
    return render(request, 'catalogo.html', context)

def servicios(request):
    mensaje = ''
    
    context = {'mensaje': mensaje,}
    return render(request, 'servicios.html', context)

def proveedores(request):
    mensaje = ''
    
    context = {'mensaje': mensaje,}
    return render(request, 'proveedores.html', context)

def contacto(request):
    mensaje = ''
    
    context = {'mensaje': mensaje,}
    return render(request, 'contacto.html', context)