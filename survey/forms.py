from django import forms
from .models import GoogleFormLink

class GoogleFormLinkForm(forms.ModelForm):
    class Meta:
        model = GoogleFormLink
        fields = ['link']