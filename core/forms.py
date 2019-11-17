from django.forms import ModelForm
from .models import usuarios


class usuariosForms(ModelForm):
	class Meta:
		model = usuarios
		fields = ['nome', 'biografia', 'email', 'idade', 'foto']

#class Cursos(ModelForm):
#class Meta():
#model
#fields = ['nome', 'curso', 'idade', 'perfil', 'periodo']
#widgets = {
#'area' : forms.RadioSelect(),(),
#'periodo' : forms.RadioSelect(),(),
#'curso' : forms.RadioSelect(),(),	
#}