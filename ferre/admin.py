# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categoria, Producto, Image, Oferta
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Image)
admin.site.register(Producto)
admin.site.register(Oferta)