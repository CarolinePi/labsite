from django import forms
from .models import TvModel, FridgeModel


class TvForm(forms.ModelForm):
    prefix = 'tv_form'

    class Meta:
        model = TvModel
        fields = ['title', 'description', 'image']


class FridgeForm(forms.ModelForm):
    prefix = 'fridge_form'

    class Meta:
        model = FridgeModel
        fields = ['title', 'description', 'image']
