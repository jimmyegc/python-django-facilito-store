from django.shortcuts import redirect, render, get_object_or_404
from .utils import get_or_create_cart
from products.models import Product
from .models import CartProducts

def cart(request):
    #Crear una sesión
    #request.session['cart_id'] = '123' #Dic
    # Obtener una sesión
    #valor = request.session.get('cart_id')
    #print(valor)
    # Eliminar sessión
    #request.session['card_id'] = None
        
    cart = get_or_create_cart(request)
    #print("cart", cart.products)
    return render(request, 'carts/cart.html', {'cart': cart})

def add(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))
    
    #cart.products.add(product, through_defaults={
    #    'quantity': quantity
    #})
    
    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart, product=product, quantity=quantity)
    
    return render(request, 'carts/add.html', { 
        'quantity': quantity,
        'cart_product': cart_product,
        'product': product
    })

def remove(request):    
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    #Product.objects.get(pk=request.POST.get('product_id'))
    
    cart.products.remove(product)
    return redirect('carts:cart')