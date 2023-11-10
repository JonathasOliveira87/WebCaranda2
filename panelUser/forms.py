from django import forms
from .models import profileManager
import re
from PIL import Image


class UpdatePhoneForm(forms.ModelForm):
    class Meta:
        model = profileManager
        fields = ['telefone']

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if not re.match(r'^\d+$', telefone):
            raise forms.ValidationError("O número de telefone deve conter apenas números.")
        return telefone


class UpdateMoradorForm(forms.ModelForm):
    class Meta:
        model = profileManager
        fields = ['morador']


class UpdateDonoForm(forms.ModelForm):
    class Meta:
        model = profileManager
        fields = ['dono']


class UpdateCasaForm(forms.ModelForm):
    class Meta:
        model = profileManager
        fields = ['casa']

    def apenasNumero(self):
        casa = self.cleaned_data.get('casa')
        if not re.match(r'^\d+$', casa):
            raise forms.ValidationError("Deve conter apenas números.")
        return casa


class UpdateCarroForm(forms.ModelForm):
    class Meta:
        model = profileManager
        fields = ['carro']


class UpdateMotoForm(forms.ModelForm):
    class Meta:
        model = profileManager
        fields = ['moto']


class UpdatePetForm(forms.ModelForm):
    class Meta:
        model = profileManager
        fields = ['pet']


class UpdatePhotoForm(forms.ModelForm):
    class Meta:
        model = profileManager
        fields = ['profile_pic']