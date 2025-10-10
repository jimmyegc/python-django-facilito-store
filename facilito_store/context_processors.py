from carts.models import Cart
from carts.utils import get_or_create_cart

def cart_item_count(request):
    count = 0
    if request.user.is_authenticated:
        cart = get_or_create_cart(request)
        if cart:
            # Filtrar solo productos con quantity > 0
            cart_products = cart.cartproducts_set.filter(quantity__gt=0)
            count = sum(cp.quantity for cp in cart_products)
    return {'cart_item_count': count}
