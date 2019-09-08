from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def inicial(request):
	dancarinos = Dancarinos.objects.all()
	contexto = {
	'dancarino': dancarinos
	}
	return render(request, 'index.html', contexto)