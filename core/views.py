from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import usuarios
from django.http import HttpResponse
from .forms import Reservar
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


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

def do_login(request):
    
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password1'])
    
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("erro")
    else:
        form = UserCreationForm()
    
    contexto = {
    'form' : form
    }
    return render(request, 'login.html', contexto)

def do_logout(request):
    logout(request)
    return redirect('index')

@login_required
def reservar(request):

    if request.method == 'POST':
        form = Reservar(request.POST or None)
    
        if form.is_valid():

            var = form.save(commit=False)
            var.cliente=request.user
            var.save()
            return redirect('index')
        else:
            return HttpResponse('erro. verifique suas informações')
    else:
        form = Reservar(initial={'cliente':request.user, 'café':True})

    contexto = {'form': Reservar}
    return render(request, 'reserva.html', contexto)    

