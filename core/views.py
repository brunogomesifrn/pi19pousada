from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import usuarios
from django.http import HttpResponse

# Create your views here.
def index(request):
	return  render(request, 'index.html') 

def cadastro(request):
	if request.method == 'POST':
		form = usuarios(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			return HttpResponse('erro. verifique suas informações')
	else:
		form = usuarios()
	contexto = {'form': form}

	return render(request, 'cadastro.html', contexto)

def login(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
	'form' : form
	}
	return render(request, 'login.html', contexto)
