from django import forms


#class that creates the form to use in html page.
class SummonerForm(forms.Form):
    name = forms.CharField()
