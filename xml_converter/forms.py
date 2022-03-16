from django import forms

class UploadXMLform(forms.Form):
    file = forms.FileField()
