from django.shortcuts import render
from liste.forms import PrestationForm, DevisForm


def test(request):
    return render(request, 'liste/test.html')


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

