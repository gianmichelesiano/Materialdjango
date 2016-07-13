# -*- coding: utf-8 -*-
from django import forms
from models import Soggetto, Registration, Gara
from material import *



class SoggetoForm(forms.ModelForm):
    class Meta:
        model = Soggetto
        #sesso = forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')))
        fields = ('ruolo', 'cognome', 'nome','indirizzo','citta','data_di_nascita','sesso',)
    layout = Layout(
        Row('ruolo', 'cognome', 'nome'),
        Row('indirizzo'),
        Row('citta'),
        Row('data_di_nascita', 'sesso'),
    )
    

class GaraForm(forms.ModelForm):
     class Meta:
         model = Gara
         fields = '__all__'
     layout = Layout(
                     Fieldset('Criteri Gara',
                     Row('tipo', 'procedura','pagamento_corrispettivo'),
                     Row('soglia'),
                     Row('oggetto_contratto'),
                     Row('progetto_base_gara'),
                     Row('criterio_aggiudicazione'),
                     )
     )
         


