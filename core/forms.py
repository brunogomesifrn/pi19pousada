from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms


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


#class Cursos(ModelForm):
#class Meta():
#model
#fields = ['nome', 'curso', 'idade', 'perfil', 'periodo']
#widgets = {
#'area' : forms.RadioSelect(),(),
#'periodo' : forms.RadioSelect(),(),
#'curso' : forms.RadioSelect(),(),  
#}