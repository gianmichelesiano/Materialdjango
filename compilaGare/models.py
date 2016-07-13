# -*- coding: cp1252 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from material import LayoutMixin, Layout, Fieldset, Inline, Row, Span2, Span5, Span7

class Shipment(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()

    # shipment address
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)


class ShipmentItem(models.Model):
    shipment = models.ForeignKey(Shipment)
    name = models.CharField(max_length=250)
    quantity = models.IntegerField(default=1)
    

SESSO_CHOICES = (
    ('M', 'Maschio'),
    ('F', 'Femmina'),
)
# Create your models here.
class Soggetto(models.Model):  
    ruolo = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    nome = models.CharField(max_length=30)
    indirizzo = models.CharField(max_length=50)
    citta = models.CharField(max_length=20)
    data_di_nascita = models.DateField(blank=True, null=True)
    sesso  = models.CharField(max_length=1, choices=SESSO_CHOICES)
    


class Registration(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    password_confirm = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')))
    receive_news =models.BooleanField()
    agree_toc = forms.BooleanField()


class Gara(models.Model):
    tipo = models.CharField(max_length=30, choices=((None, ''), ('L', 'Lavori'), ('S', 'Servizi'), ('F', 'Forniture')))
    soglia = models.CharField(max_length=30, choices=((None, ''), ('M', 'minore di 150.000'), ('C', 'compresi tra 150.000 e 1.000.000'), ('S', 'superiori a 1.000.000')))
    procedura = models.CharField(max_length=1, choices=((None, ''), ('A', 'Procedura Aperta'), ('R', 'Procedura ristretta'), ('N', 'Procedura negoziata')))
    oggetto_contratto = models.CharField(max_length=1, choices=((None, ''), ('S', 'Sola esecuzione'), ('R', 'Progettazione esecutiva ed esecuzione')))
    progetto_base_gara = models.CharField(max_length=1, choices=((None, ''), ('E', 'Progetto esecutivo'), ('D', 'Progetto definitivo'), ('T', 'Pogettazione esecutiva ed esecuzione')))
    criterio_aggiudicazione = models.CharField(max_length=1, choices=((None, ''), ('B', 'Prezzo più basso'), ('V', 'offerta economicamente più vantaggiosa')))
    pagamento_corrispettivo = models.CharField(max_length=1, choices=((None, ''), ('C', 'Corpo'), ('M', 'Misura'), ('T', 'Corpo e misura')))
    
