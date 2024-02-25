from django import forms

class CityForm(forms.Form):
    city_input = forms.CharField(label='city name...', widget=forms.Textarea)
