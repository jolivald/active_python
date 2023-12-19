from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('collaborateur', views.collaborateur_list, name="collaborateur_list"),
    path('collaborateur/<matricule>', views.collaborateur_detail, name="collaborateur_detail"),
    path('fonction', views.fonction_list, name="fonction_list"),
    path('fonction/<id>', views.fonction_detail, name="fonction_detail"),
]
