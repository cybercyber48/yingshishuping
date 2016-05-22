from django import forms

class Image_Upload_Form1(forms.Form):
    image = forms.ImageField()