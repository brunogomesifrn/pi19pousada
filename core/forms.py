from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm



class usuarios(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

#class Cursos(ModelForm):
#class Meta():
#model
#fields = ['nome', 'curso', 'idade', 'perfil', 'periodo']
#widgets = {
#'area' : forms.RadioSelect(),(),
#'periodo' : forms.RadioSelect(),(),
#'curso' : forms.RadioSelect(),(),	
#}