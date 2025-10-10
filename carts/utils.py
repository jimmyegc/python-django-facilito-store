from .models import Cart

def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')  # <-- Este debe guardar el uuid
    print("🛍 session cart_id:", cart_id)
    
    # Buscar carrito existente por UUID
    cart = Cart.objects.filter(cart_id=cart_id).first()
    print("📦 found cart:", cart)
     
    # Si no existe, crearlo
    if cart is None:
        cart = Cart.objects.create(user=user)
        print("🆕 created new cart:", cart.cart_id)
    
    # Asociar el usuario si aún no está asignado
    if user and cart.user is None:
        cart.user = user
        cart.save()
    
    # Guardar el UUID del carrito en la sesión
    request.session['cart_id'] = cart.cart_id
    print("💾 saved to session:", request.session['cart_id'])

    return cart

def destroy_cart(request):
    request.session['cart_id'] = None