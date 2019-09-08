from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def index(request):
	return  render(request, 'index.html') 


def registro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
	'form': form
	}
	return render(request, 'registro.html', contexto)