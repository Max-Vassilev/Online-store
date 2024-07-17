from django.shortcuts import render, get_object_or_404
from .cart import Cart
from online_store.store.models import TechItem
from django.http import JsonResponse


def cart_summary(request):
    return render(request, "cart/summary.html")

def add(request):
    cart = Cart(request)
    if request.POST.get("action") == 'post':
        product_id = int(request.POST.get("product_id"))
        product = get_object_or_404(TechItem, id=product_id)
        cart.add(product=product)
        response = JsonResponse({"Product Name": product.name})
        return response
