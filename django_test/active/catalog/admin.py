from django.contrib import admin

# Register your models here.
from .models import Activite, Client, Collaborateur, Contact, Contrat, Document, Etape, Fonction, Intervention, Projet

admin.site.register(Activite)
admin.site.register(Client)
admin.site.register(Collaborateur)
admin.site.register(Contact)
admin.site.register(Contrat)
admin.site.register(Document)
admin.site.register(Etape)
admin.site.register(Fonction)
admin.site.register(Intervention)
admin.site.register(Projet)
