#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Activite, Client, Collaborateur, Contact, Contrat, Document, Etape, Fonction, Intervention, Projet

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
  tpl = loader.get_template('catalog/home.html')
  ctx = {
    'options': { 'title': 'xXx Projet xXx Active xXx' },
  }
  return HttpResponse(tpl.render(ctx, request))


def activite_list(request):
  return _display_list(request, Activite.objects.all(), {
     'title': 'Activités',
     'detail': 'activite_detail',
     'primary': 'id_activite'
  })

def activite_detail(request, id):
  return _display_detail(
    request,
    'Activité',
    Activite.objects.get(id_activite=id)
  )


def client_list(request):
  return _display_list(request, Client.objects.all(), {
     'title': 'Cients',
     'detail': 'client_detail',
     'primary': 'code_client'
  })

def client_detail(request, id):
  return _display_detail(
    request,
    'Client',
    Client.objects.get(code_client=id)
  )



def collaborateur_list(request):
  return _display_list(request, Collaborateur.objects.all(), {
     'title': 'Collaborateurs',
     'detail': 'collaborateur_detail',
     'primary': 'matricule'
  })

def collaborateur_detail(request, id):
  return _display_detail(
    request,
    'Collaborateur',
    Collaborateur.objects.get(matricule=id)
  )


def contact_list(request):
  return _display_list(request, Contact.objects.all(), {
     'title': 'Contacts',
     'detail': 'contact_detail',
     'primary': 'id_contact'
  })

def contact_detail(request, id):
  return _display_detail(
    request,
    'Contact',
    Contact.objects.get(id_contact=id)
  )


def contrat_list(request):
  return _display_list(request, Contrat.objects.all(), {
     'title': 'Contrats',
     'detail': 'contrat_detail',
     'primary': 'id_contrat'
  })

def contrat_detail(request, id):
  return _display_detail(
    request,
    'Contrat',
    Contrat.objects.get(id_contrat=id)
  )


def document_list(request):
  return _display_list(request, Document.objects.all(), {
     'title': 'Documents',
     'detail': 'document_detail',
     'primary': 'id_document'
  })

def document_detail(request, id):
  return _display_detail(
    request,
    'Document',
    Document.objects.get(id_document=id)
  )


def etape_list(request):
  return _display_list(request, Etape.objects.all(), {
     'title': 'Etapes',
     'detail': 'etape_detail',
     'primary': 'num_lot'
  })

def etape_detail(request, id):
  return _display_detail(
    request,
    'Etape',
    Etape.objects.get(num_lot=id)
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


def intervention_list(request):
  return _display_list(request, Intervention.objects.all(), {
     'title': 'Interventions',
     'detail': 'intervention_detail',
     'primary': 'id_intervention'
  })

def intervention_detail(request, id):
  return _display_detail(
    request,
    'Intervention',
    Intervention.objects.get(id_intervention=id)
  )


def projet_list(request):
  return _display_list(request, Projet.objects.all(), {
     'title': 'Projets',
     'detail': 'projet_detail',
     'primary': 'code_projet'
  })

def projet_detail(request, id):
  return _display_detail(
    request,
    'Projet',
    Projet.objects.get(code_projet=id)
  )

