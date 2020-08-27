from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, required=True, label='name', widget=forms.TextInput(attrs={'class':'form-field-control-above', 'placeholder':'Name'}))
    email = forms.EmailField(required=True, label='email', widget=forms.TextInput(attrs={'class':'form-field-control-above', 'placeholder':'Email'}))
    subject = forms.CharField(max_length=100, required=True, label='subject', widget=forms.TextInput(attrs={'class':'form-field-control-above','placeholder':'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-field-control-below','placeholder':'Your message...'}), required=True, label='message')