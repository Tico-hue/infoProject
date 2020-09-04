from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def Home(request):
    return render(request,'base.html')

def Login(request):
    ingresar(request)
    return render(request,'login.html')
def LoguedIn(request):
    return render(request,'loguedIn.html')

def createUser(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
       print('PRINTING POST : ' , request.POST)
       form = CreateUserForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request,'Cuenta creada exitosamente')
        #    return redirect('Home')
    context= {'form' : form}
    return render(request,'registro.html', context)

def ingresar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)
        user = authenticate(request,username = username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Cuenta existe')
            print(request)
            return redirect('LoguedIn')
        else: 
            messages.info(request,'Usuario o contrasenia incorrectos')
    context = {}
    return render(request,'loguedIn.html',context)