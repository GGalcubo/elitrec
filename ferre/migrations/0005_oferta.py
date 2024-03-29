# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferre', '0004_auto_20161013_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.FloatField(default=0, verbose_name='Precio')),
                ('oferta', models.CharField(default=0, max_length=10, verbose_name='Oferta')),
                ('comentario', models.TextField(blank=True, null=True, verbose_name='Comentario')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ferre.Categoria')),
                ('imagen', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ferre.Image')),
            ],
        ),
    ]
