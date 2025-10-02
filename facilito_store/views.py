from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

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