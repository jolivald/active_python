#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Collaborateur, Fonction

def _display_list(request, objects, options):
  tpl = loader.get_template('catalog/list.html')
  keys = [k for k in objects[0].__dict__.keys() if k != '_state']
  ctx = {
    'options': options,
    'fields': keys,
    'values': objects,
  }
  return HttpResponse(tpl.render(ctx, request))

def _display_detail(request, title, obj):
  tpl = loader.get_template('catalog/detail.html')
  keys = [k for k in obj.__dict__.keys() if k != '_state']
  ctx = {
    'title': title,
    'fields': keys,
    'value':  obj,
  }
  return HttpResponse(tpl.render(ctx, request))

def index(request):
    return HttpResponse("Hello, world. You're at the catalog index.")

def collaborateur_list(request):
  return _display_list(request, Collaborateur.objects.all(), {
     'title': 'Collaborateurs',
     'detail': 'collaborateur_detail',
     'primary': 'matricule'
  })


def collaborateur_detail(request, matricule):
  return _display_detail(
    request,
    'Collaborateur',
    Collaborateur.objects.get(matricule=matricule)
  )

def fonction_list(request):
  return _display_list(request, Fonction.objects.all(), {
     'title': 'Fonctions',
     'detail': 'fonction_detail',
     'primary': 'id_fonction'

  })

def fonction_detail(request, id):
  return _display_detail(
    request,
    'Fonction',
    Fonction.objects.get(id_fonction=id)
  )

