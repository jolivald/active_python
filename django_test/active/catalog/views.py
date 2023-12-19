#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Collaborateur, Fonction

def _display_list(request, title, all):
  tpl = loader.get_template('catalog/list.html')
  keys = [k for k in all[0].__dict__.keys() if k != '_state']
  vals = all.__dict__.values()
  ctx = {
    'title': title,
    'fields': keys,
    'values': all,
  }
  return HttpResponse(tpl.render(ctx, request))

def _display_detail(request, title, obj):
  tpl = loader.get_template('catalog/detail.html')
  keys = [k for k in obj.__dict__.keys() if k != '_state']
  #vals = obj.__dict__.values()
  ctx = {
    'title': title,
    'fields': keys,
    'value':  obj,
  }
  return HttpResponse(tpl.render(ctx, request))

def index(request):
    return HttpResponse("Hello, world. You're at the catalog index.")

def collaborateur_list(request):
  return _display_list(
    request,
    'Collaborateur',
    Collaborateur.objects.all()
  )

def collaborateur_detail(request, matricule):
  return _display_detail(
    request,
    'Collaborateur',
    Collaborateur.objects.get(matricule=matricule)
  )

def fonction_list(request):
  return _display_list(
    request,
    'Fonction',
    Fonction.objects.all()
  )

def fonction_detail(request, id):
  return _display_detail(
    request,
    'Fonction',
    Fonction.objects.get(id_fonction=id)
  )

