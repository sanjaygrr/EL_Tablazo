from django import forms
from .models import Cliente

class CLiente_form(forms.ModelForm):
  
  class Meta:
     model = Cliente
     fields = '__all__'