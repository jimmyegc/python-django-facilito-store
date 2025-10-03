from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import RegisterForm

def index(request):
    return render(request, 'index.html', {
        'message': 'Nuevo mensaje desde HTML',
        'products': [
            { 'title': 'Computadora', 'price': 500, 'stock': True },
            { 'title': 'Teclado', 'price': 500, 'stock': False },
            { 'title': 'Monitor', 'price': 500, 'stock': True },
        ]
    })
    
def login_view (request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password) #none
        if user: 
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
            
    return render(request, 'users/login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = RegisterForm(request.POST or None) #POST se genera con lo que envia el usuario
    if request.method == 'POST' and form.is_valid():        
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado con éxito.')
            return redirect('index')
                    
    return render(request, 'users/register.html', {
        'form': form
    })