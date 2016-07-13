# -*- coding: cp1252 -*-

import extra_views
from material import LayoutMixin, Layout, Fieldset, Inline, Row, Span2, Span5, Span7
from django.shortcuts import redirect
from .forms import SoggetoForm, GaraForm
from django.shortcuts import render, get_object_or_404
from .models import Shipment, ShipmentItem, Soggetto, Registration, Gara
from django.http import HttpResponse

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import  inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class MyPrint:
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize
        
    def genera_pdf(self, titolo_doc):

    # Create the HttpResponse object with the appropriate PDF headers.
        buffer = self.buffer
        p = canvas.Canvas(buffer)
        doc = SimpleDocTemplate(buffer,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    
        Story=[]
        titolo = titolo_doc
        sottotitolo = '(redatta in conformita allALLEGATO T)'
        indirizzo = ['nomeinfirizzo', 'via_inrizzo', 'luogo_indirizzo']
        oggetto = 'OGGETTO: Dichiarazione Personale relativa ai soggetti in carica con poteri di rappresentanza, direttore tecnico, soci, amministratori.'  
        gara_testo = """Codice Esigenza n. 028712  Procedura aperta per la progettazione e l'esecuzione dei lavori di
        RISTRUTTURAZIONE EDILIZIA CON ADEGUAMENTO ALLE NORME SISMICHE DEGLI EDIFICI 1404 E 1404 BIS Localita': Roma -
        Caserma Ettore Rosso.Importo lordo a base di gara 874.175,32 di cui  41.607,00 per oneri per l'attuazionedel piano di sicurezza
        non soggetti a ribasso,  271.670,14 per costo del personale suilavori non soggetto a ribasso (art. 82 c. 3 bis D.Lgs. 163/2006),  10.708,59
        per oneri per la progettazione soggetti a ribasso ed  2.745,30 per costo del personale
        sullaprogettazione non soggetto a ribasso (art. 82 c. 3 bis D.Lgs. 163/2006)."""
        dichiarazione_soggetto_testo = u"""La sottoscritta Impresa Pinco Pallino S.r.l., con sede in Via Tizio Caio n. 1, 00100 Roma,Codice Fiscale e Partita IVA n. 012345678, Tel. 012345678, Fax 012345678, PEC pincopallino@legaltizio.it, e per essa il Sig. Pinco Caio, nato a Roma il 01.01.1985, e residente in Via Tizio n. 1, 00100 Roma, in qualità di Amministratore Unico e Legale Rappresentante pienamente consapevole della responsabilità penale cui va incontro, ai sensi e per gli effetti dell’art. 76 D.P.R. 28 dicembre 2000 n. 445, in caso di dichiarazioni mendaci o di formazione, esibizione o uso di atti falsi, ovvero di atti contenenti dati non più rispondenti a verità,"""
        dichiara = 'dichiara'
        primo_elenco = [u"""di possedere tutti i requisiti d'ordine generale di cui all'art. 38 del D.Lgs. 163/2006 e s.m.i., e più precisamente:""",'due','tre']
        seconda_lista = [u'di essere cittadino italiano;',u'l’insussistenza dello stato di fallimento, di liquidazione coatta, di concordato preventivo, o l’inesistenza di un procedimento per la dichiarazione di una di tali situazioni;']
        footer = 'Roma'
        footer_destra = 'Firma'
        
        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='titolo', alignment=TA_CENTER , fontSize=14, fontName='Times-Bold'))
        styles.add(ParagraphStyle(name='sottotitolo', alignment=TA_CENTER , fontSize=12, fontName='Times'))
        styles.add(ParagraphStyle(name='destinatario', alignment=TA_RIGHT ,fontName='Times',fontSize=12,))
        styles.add(ParagraphStyle(name='oggetto', alignment=TA_JUSTIFY ,fontName='Times-Bold',fontSize=12,leading = 16))
        styles.add(ParagraphStyle(name='normale', alignment=TA_JUSTIFY ,fontName='Times',fontSize=12,leading = 16))
        styles.add(ParagraphStyle(name='dichiara', alignment=TA_CENTER , fontSize=12, fontName='Times-Bold'))
        styles.add(ParagraphStyle(name='rientro', alignment=TA_JUSTIFY ,fontName='Times',fontSize=12,leading = 16,leftIndent = 20, bulletIndent=5, bulletFontName='Times-Roman' , bulletFontSize=12  ))
        styles.add(ParagraphStyle(name='secondo_rientro', alignment=TA_JUSTIFY ,fontName='Times',fontSize=12,leading = 16,leftIndent = 50, bulletIndent=30, bulletFontName='Times-Roman', bulletFontSize=12 ))
        styles.add(ParagraphStyle(name='footer', alignment=TA_JUSTIFY ,fontName='Times',fontSize=12 , leftIndent = 80))
        styles.add(ParagraphStyle(name='footer_destra', alignment=TA_JUSTIFY ,fontName='Times',fontSize=12 , leftIndent = 380))

        # TITOLO      
        Story.append(Paragraph(titolo, styles["titolo"]))
        Story.append(Spacer(1, 10))
        # SOTT0TITOLO    
        Story.append(Paragraph(sottotitolo, styles["sottotitolo"]))
        Story.append(Spacer(1, 20))
        # INDIRIZZO   
        for elem in indirizzo:
            Story.append(Paragraph(elem, styles["destinatario"]))
            Story.append(Spacer(1, 10))
        Story.append(Spacer(1, 20))
        # OGGETTO DICHIRAZIONE   
        Story.append(Paragraph(oggetto, styles["oggetto"]))
        Story.append(Spacer(1, 20))
        # GARA
        Story.append(Paragraph(gara_testo, styles["normale"]))
        Story.append(Spacer(1, 20))
        # SOGGETTO DICHIARANTE
        Story.append(Paragraph(dichiarazione_soggetto_testo, styles["normale"]))
        Story.append(Spacer(1, 20))
        # PAROLE DICHIARA
        Story.append(Paragraph(dichiara, styles["dichiara"]))
        Story.append(Spacer(1, 20))
        # DICHIARAZIONE
        i = 1
        for elem in primo_elenco:
            Story.append(Paragraph(elem,  styles["rientro"], bulletText=str(i)+')'))
            i = i + 1
            lettera = ord('z')
            for  due in seconda_lista:
                if lettera < 123:
                    Story.append(Paragraph(due,  styles["secondo_rientro"], bulletText=str(chr(lettera))+'.'))
                    Story.append(Spacer(1, 5))
                else:
                    new_letter = lettera-123+97
                    Story.append(Paragraph(due,  styles["secondo_rientro"], bulletText='a'+str(chr(new_letter))+'.'))
                lettera = lettera +1
            Story.append(Spacer(1, 10))
        # FINE DICHIARAZIONE
        # FOOTER         
        Story.append(Paragraph(footer, styles["footer"]))
        Story.append(Paragraph(footer_destra, styles["footer_destra"]))
        
        doc.build(Story)
        pdf = buffer.getvalue()
        buffer.close()
        return pdf
    def generaTabella(self):
        
        buffer = self.buffer
        
        p = canvas.Canvas(buffer)
        
        doc = SimpleDocTemplate(buffer,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
        elements = []
        
        indirizzo  = """fsdf
        /n fdsf
        """
        data= [['intestazione', 'intestazione'],
               ['intestazione', 'intestazione'],
               ['intestazione', 'intestazione'],
               ['Indirzzo', 'Indirzzo'],
               ['Indirzzo', 'Indirzzo'],
               [indirizzo, 'Indirzzo']]
        t=Table(data,280, 106)
        t.setStyle(TableStyle([('ALIGN',(0,0),(1,2),'CENTER'),
                               ('TEXTCOLOR',(0,0),(1,2),colors.black),
                               ('VALIGN',(0,0),(1,2),'MIDDLE'),
                               ('ALIGN',(0,3),(-1,-1),'LEFT'),
                               ('TEXTCOLOR',(0,3),(-1,-1),colors.black),
                               ('VALIGN',(0,3),(-1,-1),'MIDDLE'),
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ]))
         
        elements.append(t)
        # write the document to disk
        doc.build(elements)
        
        pdf = buffer.getvalue()
        buffer.close()
        return pdf


from io import BytesIO
def doc_base(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Documenti.pdf"'
    buffer = BytesIO()
    report = MyPrint(buffer, 'Letter')
    pdf = report.genera_pdf('capocchia')
    response.write(pdf)
    return response

def tabella(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="tabella.pdf"'
    buffer = BytesIO()
    report = MyPrint(buffer, 'Letter')
    pdf = report.generaTabella()
    response.write(pdf)
    return response



def index(request):
    soggetti = Soggetto.objects.all()
    return render(request, 'compilaGare/index.html', {'soggetti': soggetti})

 
    # OPERAZIONI SOGGETTO
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')    
def soggetto_new(request):
    if request.method == "POST":
        form = SoggetoForm(request.POST)
        if form.is_valid():
            soggetto = form.save(commit=False)
            soggetto.save()
            return redirect('compilaGare.views.soggetto_list')
    else:
        form = SoggetoForm()
    return render(request, 'compilaGare/soggetto_new.html', {'form': form})




def soggetto_detail(request, pk):
    soggetto = get_object_or_404(Soggetto, pk=pk)
    return render(request, 'compilaGare/soggetto_detail.html', {'soggetto': soggetto})


def soggetto_edit(request, pk):
    soggetto = get_object_or_404(Soggetto, pk=pk)
    if request.method == "POST":
        form = SoggetoForm(request.POST, instance=soggetto)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('compilaGare.views.soggetto_list')
    else:
        form = SoggetoForm(instance=soggetto)
    return render(request, 'compilaGare/soggetto_new.html', {'form': form})


    
def soggetto_list(request):
    soggetti = Soggetto.objects.all()
    return render(request, 'compilaGare/soggetto_list.html', {'soggetti': soggetti})
    

def gara_new(request):
    if request.method == "POST":
        form = GaraForm(request.POST)
        if form.is_valid():
            creterioGara = form.save(commit=False)
            creterioGara.save()
            #return render(request, 'compilaGare/creterioGara_new.html', {'form': form})
            return redirect('compilaGare.views.gara_list')
    else:
        form = GaraForm()

    return render(request, 'compilaGare/gara_new.html', {'form': form})
    
def gara_list(request):
    gare = Gara.objects.all()
    return render(request, 'compilaGare/gara_list.html', {'gare': gare})    

def gara_edit(request, pk):
    gara = get_object_or_404(Gara, pk=pk)
    if request.method == "POST":
        form = GaraForm(request.POST, instance=gara)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('compilaGare.views.gara_list')
    else:
        form = GaraForm(instance=gara)
    return render(request, 'compilaGare/gara_new.html', {'form': form})





