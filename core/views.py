from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import usuarios


# Create your views here.
def index(request):
	return  render(request, 'index.html') 

def cadastro(request):
	form = usuarios(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
	'form': form
	}
	return render(request, 'cadastro.html', contexto)

def login(request):
	return render(request, 'login.html')