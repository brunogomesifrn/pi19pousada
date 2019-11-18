from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Reservar 

class usuarios(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            
        }
    def __init__(self, *args, **kwargs):
        super(usuarios, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        for fieldname in ['first_name', 'last_name','username','email']:
            self.fields[fieldname].help_text = None

class Reservar(ModelForm):
    class Meta:
        model = Reservar
        fields = ['adultos', 'apartamentos', 'quantidade', 'criancas', 'cpf', 'cliente', 'cafe', 'celular', 'entrada', 'saida',]
        widgets = {
            'adultos' : forms.NumberInput(attrs={'class':'form-control'}),
            'apartamentos' : forms.SelectMultiple(attrs={'class':'form-control'}),
            'quantidade' : forms.NumberInput(attrs={'class':'form-control'}),
            'criancas' : forms.NumberInput(attrs={'class':'form-control'}),
            'cpf' : forms.NumberInput(attrs={'class':'form-control'}),
            'cliente' : forms.HiddenInput(attrs={'class':'form-control'}),
            'cafe' : forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'celular' : forms.NumberInput(attrs={'class':'form-control'}),
            'entrada' : forms.DateInput(attrs={'class':'form-control', 'type' : 'date'}),
            'saida' : forms.DateInput(attrs={'class':'form-control', 'type' : 'date'}), 
   
        }


#class Cursos(ModelForm):
#class Meta():
#model
#fields = ['nome', 'curso', 'idade', 'perfil', 'periodo']
#widgets = {
#'area' : forms.RadioSelect(),(),
#'periodo' : forms.RadioSelect(),(),
#'curso' : forms.RadioSelect(),(),  
#}