# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activite(models.Model):
    id_activite = models.AutoField(primary_key=True)
    libelle_activite = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'activite'
        
    # string representation of the model (also used in django admin)
    def __str__(self):
        return self.libelle_activite


class Client(models.Model):
    code_client = models.CharField(primary_key=True, max_length=4)
    type_client = models.CharField(max_length=1)
    domaine_activite = models.CharField(max_length=100)
    nature_activite = models.CharField(max_length=10)
    raison_sociale = models.CharField(max_length=100)
    chiffre_affaires = models.IntegerField()
    effectifs = models.IntegerField()
    commentaires_commerciaux_client = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'

    # string representation of the model (also used in django admin)
    def __str__(self):
        return self.raison_sociale


class Collaborateur(models.Model):
    matricule = models.CharField(primary_key=True, max_length=4)
    nom_collaborateur = models.CharField(max_length=20)
    prenom_collaborateur = models.CharField(max_length=20)
    sexe_collaborateur = models.CharField(max_length=1)
    etat_civil_collaborateur = models.CharField(max_length=3)
    id_fonction = models.ForeignKey('Fonction', models.DO_NOTHING, db_column='id_fonction')

    class Meta:
        managed = False
        db_table = 'collaborateur'

    # string representation of the model (also used in django admin)
    def __str__(self):
        return self.prenom_collaborateur + " " + self.nom_collaborateur


class Contact(models.Model):
    id_contact = models.AutoField(primary_key=True)
    nom_contact = models.CharField(max_length=20)
    prenom_contact = models.CharField(max_length=20)
    email_contact = models.CharField(max_length=50)
    tel_contact = models.CharField(max_length=10)
    code_projet = models.ForeignKey('Projet', models.DO_NOTHING, db_column='code_projet')
    code_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='code_client')

    class Meta:
        managed = False
        db_table = 'contact'

    # string representation of the model (also used in django admin)
    def __str__(self):
        return self.prenom_contact + ' ' + self.nom_contact


class Contrat(models.Model):
    id_contrat = models.AutoField(primary_key=True)
    date_debut_contrat = models.DateField()
    date_fin_contrat = models.DateField(blank=True, null=True)
    libelle_contrat = models.CharField(max_length=50, blank=True, null=True)
    salaire = models.DecimalField(max_digits=19, decimal_places=4)
    type = models.CharField(max_length=3)
    matricule = models.ForeignKey(Collaborateur, models.DO_NOTHING, db_column='matricule')

    class Meta:
        managed = False
        db_table = 'contrat'
        
    # string representation of the model (also used in django admin)
    def __str__(self):
        return self.type + ' ' + self.libelle_contrat


class Document(models.Model):
    id_document = models.AutoField(primary_key=True)
    titre_document = models.CharField(max_length=100)
    resume_document = models.CharField(max_length=1000)
    date_diffusion_document = models.DateField()
    code_projet = models.ForeignKey('Projet', models.DO_NOTHING, db_column='code_projet')
    matricule = models.ForeignKey(Collaborateur, models.DO_NOTHING, db_column='matricule')

    class Meta:
        managed = False
        db_table = 'document'
        
    # string representation of the model (also used in django admin)
    def __str__(self):
        return self.titre_document


class Etape(models.Model):
    num_lot = models.CharField(primary_key=True, max_length=6)
    charge_estimee = models.SmallIntegerField()
    charge_reelle_prod = models.SmallIntegerField(blank=True, null=True)
    charge_reelle_validation = models.SmallIntegerField(blank=True, null=True)
    id_activite = models.ForeignKey(Activite, models.DO_NOTHING, db_column='id_activite')
    code_projet = models.ForeignKey('Projet', models.DO_NOTHING, db_column='code_projet')

    class Meta:
        managed = False
        db_table = 'etape'
        
    # string representation of the model (also used in django admin)
    def __str__(self):
        return self.num_lot + ' - ' + self.id_activite


class Fonction(models.Model):
    id_fonction = models.AutoField(primary_key=True)
    libelle_fonction = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'fonction'
        
    # string representation of the model (also used in django admin)
    def __str__(self):
        return self.libelle_fonction


class Intervention(models.Model):
    id_intervention = models.AutoField(primary_key=True)
    date_debut_intervention = models.DateField()
    date_fin_intervention = models.DateField()
    libelle_intervention = models.CharField(max_length=100)
    matricule = models.ForeignKey(Collaborateur, models.DO_NOTHING, db_column='matricule')
    num_lot = models.ForeignKey(Etape, models.DO_NOTHING, db_column='num_lot')
    id_fonction = models.ForeignKey(Fonction, models.DO_NOTHING, db_column='id_fonction')

    class Meta:
        managed = False
        db_table = 'intervention'
        
    # string representation of the model (also used in django admin)
    def __str__(self):
        return self.libelle_intervention


class Projet(models.Model):
    code_projet = models.CharField(primary_key=True, max_length=4)
    libelle_long_projet = models.CharField(max_length=50)
    libelle_court_projet = models.CharField(max_length=10)
    type_projet = models.CharField(max_length=1)
    cycle_vie_projet = models.CharField(max_length=10)
    infos_techniques_projet = models.CharField(max_length=100)
    charge_estimee_projet = models.SmallIntegerField()
    remarques_estimation_projet = models.CharField(max_length=100)
    date_debut_prevue = models.DateField()
    date_fin_prevue = models.DateField()
    date_debut_reelle = models.DateField(blank=True, null=True)
    date_fin_reelle = models.DateField(blank=True, null=True)
    equipe_max_projet = models.SmallIntegerField()
    commentaires_commerciaux_projet = models.CharField(max_length=255, blank=True, null=True)
    secteur_activite = models.CharField(max_length=50)
    matricule = models.ForeignKey(Collaborateur, models.DO_NOTHING, db_column='matricule')
    code_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='code_client')

    class Meta:
        managed = False
        db_table = 'projet'
        
    # string representation of the model (also used in django admin)
    def __str__(self):
        return self.code_projet + ' - ' + self.libelle_long_projet

