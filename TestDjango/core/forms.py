from django import forms
from django.forms import ModelForm
from .models import Cliente, Pais

class CLiente_form(forms.ModelForm):
  
  class Meta:
     password = forms.CharField(widget=forms.PasswordInput())
     model = Cliente
     fields = ['identificacion','telefono','nombre','email','constraseña','pais']
