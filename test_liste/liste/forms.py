from django import forms
from liste.models import Prestation, Devis, Facturation

import calculation


class TestForm(forms.ModelForm):
    total = forms.DecimalField(
        widget=calculation.FormulaInput('qte*prix') # <- using single math expression
    )
    #apply_tax = forms.BooleanField(initial=True)
    tax = forms.DecimalField(
        # using math expression and javascript functions.
        widget=calculation.FormulaInput('apply_tax ? parseFloat(total/11).toFixed(2) : 0.0')
    )

    class Meta:
        model = Facturation
        fields = '__all__'


class PrestationForm(forms.ModelForm):
    class Meta:
        model = Prestation
        fields = '__all__'

class DevisForm(forms.ModelForm):
    class Meta:
        model = Devis
        fields = '__all__'
