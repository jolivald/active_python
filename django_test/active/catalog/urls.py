from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('activite', views.activite_list, name="activite_list"),
    path('activite/<id>', views.activite_detail, name="activite_detail"),
    
    path('client', views.client_list, name="client_list"),
    path('client/<id>', views.client_detail, name="client_detail"),

    path('collaborateur', views.collaborateur_list, name="collaborateur_list"),
    path('collaborateur/<id>', views.collaborateur_detail, name="collaborateur_detail"),

    path('contact', views.contact_list, name="contact_list"),
    path('contact/<id>', views.contact_detail, name="contact_detail"),

    path('contrat', views.contrat_list, name="contrat_list"),
    path('contrat/<id>', views.contrat_detail, name="contrat_detail"),

    path('document', views.document_list, name="document_list"),
    path('document/<id>', views.document_detail, name="document_detail"),

    path('etape', views.etape_list, name="etape_list"),
    path('etape/<id>', views.etape_detail, name="etape_detail"),

    path('fonction', views.fonction_list, name="fonction_list"),
    path('fonction/<id>', views.fonction_detail, name="fonction_detail"),

    path('intervention', views.intervention_list, name="intervention_list"),
    path('intervention/<id>', views.intervention_detail, name="intervention_detail"),

    path('projet', views.projet_list, name="projet_list"),
    path('projet/<id>', views.projet_detail, name="projet_detail"),

]
