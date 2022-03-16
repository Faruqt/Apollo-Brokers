from django import forms

class Upload_XML_form(forms.Form):
    file = forms.FileField()
