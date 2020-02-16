from django import forms
from .models import CitiesWeather


class CityForm(forms.ModelForm):
    class Meta:
        model = CitiesWeather
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Add City'})}