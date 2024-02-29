from django import forms
from liste.models import Prestation, Devis


class PrestationForm(forms.ModelForm):
    class Meta:
        model = Prestation
        fields = '__all__'

class DevisForm(forms.ModelForm):
    class Meta:
        model = Devis
        fields = '__all__'
