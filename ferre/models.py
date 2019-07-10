# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    comentario = models.TextField('Comentario', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Image(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    image = models.ImageField(upload_to="images/", null=True, blank=True, default='sin_imagen.jpg')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField('Precio', default=0)
    oferta = models.CharField('Oferta', max_length=10, default=0)
    categoria = models.ForeignKey(Categoria)
    imagen = models.ForeignKey(Image, default='')
    comentario = models.TextField('Comentario', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Oferta(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField('Precio', default=0)
    oferta = models.CharField('Oferta', max_length=10, default=0)
    categoria = models.ForeignKey(Categoria)
    imagen = models.ForeignKey(Image, default='')
    comentario = models.TextField('Comentario', null=True, blank=True)

    def __str__(self):
        return self.nombre
