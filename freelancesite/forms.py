from django import forms
from .models import ContactForm
from django.forms import ModelForm

"""class ContactForm(forms.Form):
    name = forms.CharField(label='Your name')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

"""


class ContactForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'

