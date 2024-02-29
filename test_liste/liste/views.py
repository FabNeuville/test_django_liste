from django.shortcuts import render
from liste.forms import PrestationForm, DevisForm, TestForm

from django.http import JsonResponse
from .models import Prestation

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def get_artiste(request, artiste_id):
    titre_spectacle = Prestation.objects.get(id=artiste_id).titre_spectacle
    nb_artiste = Prestation.objects.get(id=artiste_id).nb_artiste
    nb_technicien = Prestation.objects.get(id=artiste_id).nb_technicien
    duree_spectacle = Prestation.objects.get(id=artiste_id).duree_spectacle.strftime('%H:%M')
    cachet_ttc = Prestation.objects.get(id=artiste_id).cachet_ttc

    return JsonResponse({'titre_spectacle': titre_spectacle,
                         'nb_artiste': nb_artiste,
                         'nb_technicien': nb_technicien,
                         'duree_spectacle': duree_spectacle,
                         'cachet_ttc': cachet_ttc,
                         })


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")


def test(request):
    return render(request, 'liste/test.html')


def calcul(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            facturation = form.save()
            return render(request, 'liste/test.html')
    else:
        form = TestForm()

    return render(request, 'liste/calcul.html', {'form': form})


def prestation_create(request):
    if request.method == 'POST':
        form = PrestationForm(request.POST)
        if form.is_valid():
            prestation = form.save()
            return render(request, 'liste/test.html')
    else:
        form = PrestationForm()

    return render(request, 'liste/prestation_create.html', {'form': form})

def devis_create(request):
    if request.method == 'POST':
        form = DevisForm(request.POST)
        if form.is_valid():
            devis = form.save()
            return render(request, 'liste/test.html')
    else:
        form = DevisForm()

    return render(request, 'liste/devis_create.html', {'form': form})

