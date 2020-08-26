from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField()